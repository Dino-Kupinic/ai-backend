// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  modules: ["@nuxt/ui", "@nuxt/eslint", "@nuxtjs/mdc"],
  css: ["~/assets/css/main.css"],
  components: [
    {
      global: true,
      path: "~/components",
      pathPrefix: false,
    },
  ],
  runtimeConfig: {
    public: {
      API_URL: process.env.API_URL,
    },
  },
  mdc: {
    components: {
      prose: true,
    },
  },
  colorMode: {
    preference: "light",
  },
  typescript: {
    typeCheck: true,
    strict: true,
  },
})
