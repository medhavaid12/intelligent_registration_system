const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://127.0.0.1:8000',
    specPattern: 'automation/cypress/e2e/**/*.js',
    supportFile: false,
    video: true,
    videosFolder: 'cypress/videos'
  }
})
