<script setup lang="ts">
const links = [
  [
    {
      label: "Profile",
      avatar: {
        src: "https://api.dicebear.com/9.x/initials/svg?seed=Dino%20Kupinic",
      },
      to: "/settings",
      badge: "Pro",
    },
  ],
  [
    {
      label: "Lorem Ipsum Dolor Sit Amet",
    },
  ],
]
</script>

<template>
  <UVerticalNavigation
    :links="links"
    :ui="{
      badge: {
        color: 'primary',
        variant: 'subtle',
      },
    }"
    class="w-64 overflow-y-auto border-r border-neutral-200 p-2 dark:border-neutral-800"
  />
</template>
