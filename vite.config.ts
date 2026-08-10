import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
  build: {
    outDir: 'static/assets',
    emptyOutDir: false,
    rollupOptions: {
      input: 'static/src/style.css',
      output: {
        assetFileNames: 'style.css',
      },
    },
  },
})
