module.exports = {
  apps: [
    {
      name: 'olotc-client',
      cwd: `./client`,
      // exec_mode: 'cluster',
      // instances: 'max', // Or a number of instances
      script: './node_modules/nuxt/bin/nuxt.js',
      args: 'start',
      watch: true,
      restart: true,
    },
    {
      name: "olotc-server",
      cwd: `./server`,
      script: "../../venv/bin/gunicorn --workers=2 -b 0.0.0.0:5000 --worker-class=meinheld.gmeinheld.MeinheldWorker wsgi:app",
      // script: "gunicorn --workers=2 -b 0.0.0.0:5000 --worker-class=meinheld.gmeinheld.MeinheldWorker wsgi:app",
      watch: false,
      max_memory_restart: "256M",
      output: "./logs/olotc-out.log",
      error: "./logs/olotc-error.log",
      kill_timeout: 5000,
      restartDelay: 5000,
      restart: true,
    }
  ]
}