// @ts-expect-error The nuxt-ui package installs tailwindcss
import type { Config } from "tailwindcss"

export default <Partial<Config>>{
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--gradient-color-stops))",
      },
    },
  },
}
