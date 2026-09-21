/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
  ],
  theme: {
    extend: {
      colors: {
        // Твоя нова мінімалістична палітра
        'mit-bg': '#FAFAFA',       // Теплий білий фон (як аркуш паперу)
        'mit-text': '#2D3748',     // М'який графіт для основного тексту
        'mit-muted': '#8E8E93',    // Світло-сірий для другорядних написів (Apple style)
        'mit-surface': '#F3F4F6',  // Трохи темніший фон для виділення карток/меню
        'mit-accent': '#C7D2FE',   // Пастельний індиго для акцентів (можна змінити на пудрово-кораловий #FECDD3, якщо хочеш відсилку до червоного)
      },
      fontFamily: {
        // Системні шрифти для максимальної швидкості та нативності (як у Apple)
        sans: ['-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'Helvetica', 'Arial', 'sans-serif'],
      }
    },
  },
  plugins: [],
}