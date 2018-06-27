const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: [
    // Specify scss files
    path.join(__dirname,'static','materialize', 'sass', 'materialize.scss')
  ],
  output: {
    filename: 'static/js/bundle.js'
  },
  module: {
    // Add loader
    rules: [{
      test: /\.(scss)$/,
      loader: ExtractTextPlugin.extract(['css-loader', 'sass-loader'])
    }]
  },
  plugins: [
    // Specify output file name and path
    new ExtractTextPlugin({
      filename: 'static/css/style.css'
    })
  ]
};