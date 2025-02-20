const { defineConfig } = require('@vue/cli-service');

module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: "http://flask_app:5000", // Nombre del contenedor en Docker
        changeOrigin: true,
        pathRewrite: { "^/api": "" },
      },
    },
  },
};
