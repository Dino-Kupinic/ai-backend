import {DefaultTheme} from "vitepress";

export default {
  title: "AI Backend",
  description: "✨ powered by llama3",
  themeConfig: {
    nav: nav(),
  },
  editLink: {
    pattern: "https://github.com/Dino-Kupinic/ai-backend/edit/main/docs/:path",
    text: "Edit this page on GitHub"
  },
  lastUpdated: {
    text: 'Last Updated at',
  },
  footer: {
    message: "Released under the MIT License.",
    copyright: "Copyright © 2024-present Dino Kupinic",
  },
}

function nav(): DefaultTheme.NavItem[] {
  return [
    {
      text: "Home",
      link: "/",
    },
    {
      text: "Guide",
      link: "/guide/getting-started",
    },
  ]
}
