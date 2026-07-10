#!/usr/bin/env python3
"""Update the generated latest-projects section in README.md."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


OWNER = os.environ.get("PROFILE_OWNER", "muneeb-anjum0")
PROFILE_REPO = os.environ.get("PROFILE_REPO", "muneeb-anjum0")
README = Path(os.environ.get("README_PATH", "README.md"))
START = "<!-- latest-projects:start -->"
END = "<!-- latest-projects:end -->"
PANEL_EXTRA_PADDING = 48


def api_json(path: str):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8")), response.headers


def api_count(path: str) -> int:
    data, headers = api_json(f"{path}{'&' if '?' in path else '?'}per_page=1")
    link = headers.get("Link", "")
    match = re.search(r"[?&]page=(\d+)>; rel=\"last\"", link)
    if match:
        return int(match.group(1))
    return len(data) if isinstance(data, list) else 0


def format_date(value: str) -> str:
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed.strftime("%Y-%m-%d")


def tag(label: str, value: str | int) -> str:
    return f"<kbd><b>{label}: {value}</b></kbd>"


def command_panel(command: str, target_length: int) -> str:
    spacer = "&nbsp;" * max(0, target_length - len(command))
    prompt = "PS&nbsp;C:\\Users\\MUNEEB&gt;&nbsp;"
    command_text = command.replace("-", "&#8209;")
    return "\n".join(
        [
            "<table>",
            "  <tr>",
            f"    <td width=\"100%\"><samp>{prompt}{command_text}{spacer}</samp></td>",
            "  </tr>",
            "</table>",
        ]
    )


def repo_description(repo: dict) -> str:
    description = (repo.get("description") or "").strip()
    if description:
        return description.rstrip(".") + "."
    return "Recently updated project repository."


def fetch_latest_repos() -> list[dict]:
    repos, _ = api_json(
        f"/users/{OWNER}/repos?"
        + urllib.parse.urlencode(
            {
                "type": "owner",
                "sort": "pushed",
                "direction": "desc",
                "per_page": "100",
            }
        )
    )
    projects = [
        repo
        for repo in repos
        if repo["name"] != PROFILE_REPO and not repo.get("fork")
    ]
    return projects[:3]


def render_project(repo: dict, target_command_length: int) -> str:
    name = repo["name"]
    default_branch = repo.get("default_branch") or "main"
    language = repo.get("language") or "Mixed"
    commits = api_count(f"/repos/{OWNER}/{name}/commits?sha={default_branch}")
    prs = api_count(f"/repos/{OWNER}/{name}/pulls?state=all")
    pushed = format_date(repo["pushed_at"])

    tags = " ".join(
        [
            tag("Language", language),
            tag("Commits", commits),
            tag("PRs", prs),
            tag("Last pushed", pushed),
        ]
    )

    return "\n".join(
        [
            f"### [{name}]({repo['html_url']})",
            "",
            command_panel(f"Open-{name}", target_command_length),
            "",
            repo_description(repo),
            "",
            tags,
        ]
    )


def main() -> int:
    try:
        projects = fetch_latest_repos()
        if len(projects) < 3:
            raise RuntimeError("Expected at least three project repositories.")

        commands = [f"Open-{repo['name']}" for repo in projects]
        target_command_length = max(len(command) for command in commands)
        target_command_length += PANEL_EXTRA_PADDING
        generated = "\n\n".join(
            render_project(repo, target_command_length) for repo in projects
        )
        replacement = f"{START}\n{generated}\n{END}"

        readme = README.read_text(encoding="utf-8")
        pattern = re.compile(
            rf"{re.escape(START)}.*?{re.escape(END)}",
            flags=re.DOTALL,
        )
        if not pattern.search(readme):
            raise RuntimeError("README markers were not found.")

        README.write_text(
            pattern.sub(lambda _match: replacement, readme),
            encoding="utf-8",
        )
        return 0
    except (urllib.error.URLError, RuntimeError, KeyError) as exc:
        print(f"update_latest_projects failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
