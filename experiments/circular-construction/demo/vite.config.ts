import { defineConfig } from 'vite';

export default defineConfig({
  base: './',
  build: {
    rollupOptions: {
      input: {
        experience: 'index.html',
        workcell: 'workcell.html',
        lab: 'lab.html',
        climb: 'climb.html',
        architecture: 'architecture.html',
      },
    },
  },
});
