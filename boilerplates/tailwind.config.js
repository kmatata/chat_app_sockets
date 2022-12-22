/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../chatApp/templates/**/*.html",
            "../chatApp/templates/*.html"
          ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}
