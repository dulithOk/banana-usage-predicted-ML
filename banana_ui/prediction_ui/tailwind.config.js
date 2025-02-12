/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'], // Specify where Tailwind should look for classes
  theme: {
    extend: {}, // Use this to extend the default Tailwind theme
  },
  plugins: [], // Add Tailwind plugins here if needed
};
