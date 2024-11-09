/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.{html,js}"],
  darkMode : "class",
  theme: {
    extend: {

      fontFamily : {
        'atyp-bold' : 'atyp-bold',
        'atyp-normal' : 'atyp-normal'
      },

      colors : {
        'my-gray' : 'rgb(192 192 192)',
        'my-orange' : 'rgb(242 66 12)',
      }

    },
  },
  plugins: [],
}

