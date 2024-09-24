/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      fontFamily: {
        'sans': ["Atkinson Hyperlegible", ...defaultTheme.fontFamily.sans]
      },
      colors: {
        primary: "#3c7dc1",
      },
    },
  },
  plugins: [
    require("@tailwindcss/typography"),
    require('daisyui'),
  ],
  daisyui: {
    themes: ["light"],
  },
};
