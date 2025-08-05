<script setup lang="ts">
import type { NavigationMenuItem } from "@nuxt/ui"

const items = ref<NavigationMenuItem[][]>([
  [
    {
      label: "Chat",
      type: "label"
    },
    {
      label: "How to cook a meal",
      icon: "i-lucide-message-square-text",
      to: "/"
    },
    {
      label: "Archive",
      type: "label"
    },
    {
      label: "Yesterday",
      icon: "i-lucide-calendar",
      defaultOpen: true,
      children: [
        {
          label: "Introduction",
          description: "Fully styled and customizable components for Nuxt.",
          icon: "i-lucide-house"
        },
        {
          label: "Installation",
          description:
            "Learn how to install and configure Nuxt UI in your application.",
          icon: "i-lucide-cloud-download"
        },
        {
          label: "Icons",
          icon: "i-lucide-smile",
          description:
            "You have nothing to do, @nuxt/icon will handle it automatically."
        },
        {
          label: "Colors",
          icon: "i-lucide-swatch-book",
          description:
            "Choose a primary and a neutral color from your Tailwind CSS theme."
        },
        {
          label: "Theme",
          icon: "i-lucide-cog",
          description:
            "You can customize components by using the `class` / `ui` props or in your app.config.ts."
        }
      ]
    }
  ]
])

const items2 = ref<NavigationMenuItem[]>([
  {
    label: "GitHub",
    icon: "i-simple-icons-github",
    to: "https://github.com/nuxt/ui",
    target: "_blank"
  },
  {
    label: "Help",
    icon: "i-lucide-circle-help"
  }
])

const items3 = ref<NavigationMenuItem[]>([
  {
    label: "Profile",
    avatar: {
      src: "https://api.dicebear.com/9.x/initials/svg?seed=Dino%20Kupinic"
    },
    to: "/settings",
    badge: "Pro"
  }
])
</script>

<template>
  <div
    class="flex h-dvh min-w-56 flex-col justify-between border-r border-neutral-200 dark:border-neutral-800"
  >
    <div class="grow">
      <div
        class="border-b border-neutral-200 pt-1 pr-2 pb-2 dark:border-neutral-800"
      >
        <UNavigationMenu
          orientation="vertical"
          :items="items3"
          color="primary"
          :highlight="true"
        />
      </div>
      <UNavigationMenu
        orientation="vertical"
        :items="items"
        color="primary"
        :highlight="true"
        class="h-full grow-0 overflow-y-auto"
      />
    </div>
    <UNavigationMenu
      orientation="vertical"
      :items="items2"
      color="primary"
      class="grow-0 border-t border-neutral-200 dark:border-neutral-800"
    />
  </div>
</template>
