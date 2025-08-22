<!-- README.md -->

<!-- ===== macOS Terminal — Animated Inline SVG ===== -->
<div align="center">

<!-- Inline animated SVG (no external JS) -->
<svg width="980" height="260" viewBox="0 0 980 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Muneeb Anjum — Full-Stack Engineer">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b0e14"/>
      <stop offset="100%" stop-color="#121826"/>
    </linearGradient>
    <linearGradient id="barGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#12151f"/>
      <stop offset="100%" stop-color="#0f1320"/>
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: "SFMono-Regular", Menlo, Consolas, "Liberation Mono", monospace; }
    .ui   { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji"; }
    @keyframes blink { 0%,49%{opacity:1} 50%,100%{opacity:0} }
    .caret { animation: blink 1s steps(1) infinite; }
    @keyframes scroll {
      0%   { transform: translateY(0); }
      45%  { transform: translateY(-26px); }
      55%  { transform: translateY(-26px); }
      100% { transform: translateY(-52px); }
    }
    .scroll { animation: scroll 12s linear infinite; }
    @keyframes scan {
      0%   { stroke-dashoffset: 480; opacity: .12; }
      50%  { opacity: .28; }
      100% { stroke-dashoffset: 0; opacity: .12; }
    }
    .scanline {
      stroke: #00e676;
      stroke-width: 1;
      stroke-dasharray: 480;
      animation: scan 6s linear infinite;
    }
    @keyframes pulse { 0%,100% { opacity:.5 } 50% { opacity:1 } }
    .pulse { animation: pulse 2.4s ease-in-out infinite; }
  </style>

  <!-- Window -->
  <rect x="0" y="0" width="980" height="260" rx="14" fill="url(#bgGrad)"/>
  <!-- Top bar -->
  <rect x="0" y="0" width="980" height="44" rx="14" fill="url(#barGrad)"/>
  <!-- Traffic lights -->
  <circle cx="28" cy="22" r="6.5" fill="#ff5f57"/>
  <circle cx="48" cy="22" r="6.5" fill="#febc2e"/>
  <circle cx="68" cy="22" r="6.5" fill="#28c840"/>
  <!-- Title -->
  <text x="90" y="27" class="mono" font-size="13" fill="#9aa5b1">muneeb@github — zsh</text>

  <!-- Content area -->
  <g transform="translate(30,68)">
    <!-- Big name -->
    <text x="0" y="0" class="ui" font-weight="700" font-size="28" fill="#e6edf3">Muneeb Anjum</text>
    <text x="0" y="28" class="ui" font-size="16" fill="#a7b0bf">Full-Stack Engineer · React · TypeScript · .NET · MERN</text>

    <!-- Prompt + lines -->
    <g transform="translate(0,56)">
      <!-- prompt shadow -->
      <text x="0" y="0" class="mono pulse" font-size="16" fill="#00e676" opacity=".35">$</text>
      <!-- prompt -->
      <text x="0" y="0" class="mono" font-size="16" fill="#00e676">$</text>
      <text x="16" y="0" class="mono" font-size="16" fill="#9aa5b1">whoami</text>
      <text x="0" y="26" class="mono" font-size="16" fill="#00e676">$</text>
      <text x="16" y="26" class="mono" font-size="16" fill="#9aa5b1">stack --show</text>

      <!-- scrolling output -->
      <g class="scroll" transform="translate(0,6)">
        <text x="140" y="0" class="mono" font-size="16" fill="#cdd6e3">→ Muneeb Anjum</text>
        <text x="140" y="26" class="mono" font-size="16" fill="#cdd6e3">→ React • TypeScript • .NET • Node • Express • MongoDB • PostgreSQL • Azure • Docker</text>
        <text x="140" y="52" class="mono" font-size="16" fill="#cdd6e3">→ Muneeb Anjum</text>
        <text x="140" y="78" class="mono" font-size="16" fill="#cdd6e3">→ React • TypeScript • .NET • Node • Express • MongoDB • PostgreSQL • Azure • Docker</text>
      </g>

      <!-- caret (blinking) -->
      <rect x="128" y="-12" width="9" height="20" fill="#00e676" class="caret" rx="2" />
    </g>
  </g>

  <!-- Scanline -->
  <line x1="20" y1="248" x2="960" y2="248" class="scanline"/>
</svg>
</div>

---

<!-- Centered Name + Typing line -->
<div align="center">

<h1>🧑‍💻 Muneeb Anjum</h1>
<h3>Full-Stack Engineer · React · .NET · MERN</h3>

<a href="https://github.com/muneeb-anjum0">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2600&pause=700&color=00E676&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=90&lines=muneeb%40github~%24+whoami;Building+fast%2C+resilient+web+apps+%7C+Performance+%E2%80%A2+Reliability+%E2%80%A2+DX"
    alt="typing animation"
  />
</a>

<sub>🔴 🟡 🟢  —  macOS-style terminal</sub>
</div>

---

<!-- Quick Links -->
<p align="center">
  <a href="mailto:muneeb.anjum@hotmail.com">
    <img src="https://img.shields.io/badge/Email-Contact-000?style=for-the-badge&logo=minutemailer&logoColor=00e676&labelColor=000&color=111"/>
  </a>
  <a href="https://www.linkedin.com/in/muneebanjum335">
    <img src="https://img.shields.io/badge/LinkedIn-muneebanjum335-000?style=for-the-badge&logo=linkedin&logoColor=00e676&labelColor=000&color=111"/>
  </a>
  <a href="https://muneeb-anjum0.github.io/Portfolio_Website/">
    <img src="https://img.shields.io/badge/Portfolio-Visit-000?style=for-the-badge&logo=vercel&logoColor=00e676&labelColor=000&color=111"/>
  </a>
  <img src="https://komarev.com/ghpvc/?username=muneeb-anjum0&label=Views&color=00e676&style=for-the-badge"/>
  <img src="https://img.shields.io/github/followers/muneeb-anjum0?style=for-the-badge&label=Followers&color=00e676&labelColor=000">
  <img src="https://img.shields.io/github/stars/muneeb-anjum0?style=for-the-badge&label=Stars&color=00e676&labelColor=000">
</p>

## 🧷 What I Do
- Turn polished designs into systems that stay fast under load  
- Ship mobile-first UIs with type-safe APIs  
- MERN core; fluent in **.NET**, **SQL/NoSQL**, **Azure**  
- Obsessed with **performance**, **reliability**, **DX**

---

## 🔧 Tech (clickable)
<p align="center">
  <a href="https://react.dev/"><img src="https://skillicons.dev/icons?i=react" height="40"/></a>
  <a href="https://nodejs.org/"><img src="https://skillicons.dev/icons?i=nodejs" height="40"/></a>
  <a href="https://expressjs.com/"><img src="https://skillicons.dev/icons?i=express" height="40"/></a>
  <a href="https://www.mongodb.com/"><img src="https://skillicons.dev/icons?i=mongodb" height="40"/></a>
  <a href="https://www.postgresql.org/"><img src="https://skillicons.dev/icons?i=postgres" height="40"/></a>
  <a href="https://www.typescriptlang.org/"><img src="https://skillicons.dev/icons?i=ts" height="40"/></a>
  <a href="https://developer.mozilla.org/docs/Web/JavaScript"><img src="https://skillicons.dev/icons?i=js" height="40"/></a>
  <a href="https://tailwindcss.com/"><img src="https://skillicons.dev/icons?i=tailwind" height="40"/></a>
  <a href="https://dotnet.microsoft.com/"><img src="https://skillicons.dev/icons?i=dotnet" height="40"/></a>
  <a href="https://www.python.org/"><img src="https://skillicons.dev/icons?i=python" height="40"/></a>
  <a href="https://azure.microsoft.com/"><img src="https://skillicons.dev/icons?i=azure" height="40"/></a>
  <a href="https://git-scm.com/"><img src="https://skillicons.dev/icons?i=git" height="40"/></a>
  <a href="https://github.com/"><img src="https://skillicons.dev/icons?i=github" height="40"/></a>
  <a href="https://www.prisma.io/"><img src="https://skillicons.dev/icons?i=prisma" height="40"/></a>
  <a href="https://www.postman.com/"><img src="https://skillicons.dev/icons?i=postman" height="40"/></a>
  <a href="https://www.docker.com/"><img src="https://skillicons.dev/icons?i=docker" height="40"/></a>
</p>

---

## ✨ Terminal Cards
<div align="center">
<pre>
muneeb@git:~$ npx create-app --stack React,.NET,MERN --host azure
✔ API design: type-safe, clean
✔ DB: SQL/NoSQL, practical modeling
✔ Perf: caching, pagination, profiling
</pre>

<pre>
muneeb@git:~$ ship --reliability --observability --dx
✔ Health checks   ✔ CI/CD   ✔ Error budgets
</pre>
</div>

---

## ⭐ Featured Projects
<table>
  <tr>
    <td>
      <a href="https://github.com/muneeb-anjum0/SortingVisualizer">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=muneeb-anjum0&repo=SortingVisualizer&theme=transparent&border_color=30363d" alt="SortingVisualizer">
      </a>
    </td>
    <td>
      <a href="https://github.com/muneeb-anjum0/Match-Three">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=muneeb-anjum0&repo=Match-Three&theme=transparent&border_color=30363d" alt="Match-Three">
      </a>
    </td>
  </tr>
</table>

---

## 📊 Stats
<p align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=muneeb-anjum0&show_icons=true&theme=transparent&hide_title=true&border_color=30363d" alt="stats">
  <img height="170" src="https://github-readme-streak-stats.herokuapp.com?user=muneeb-anjum0&theme=transparent&hide_border=true" alt="streak">
</p>

---

## 🐍 Contribution Snake
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/muneeb-anjum0/muneeb-anjum0/output/github-snake-dark.svg" />
    <img alt="github-snake" src="https://raw.githubusercontent.com/muneeb-anjum0/muneeb-anjum0/output/github-snake.svg" />
  </picture>
</p>
