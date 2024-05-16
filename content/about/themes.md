---
title: "The Theme System"
draft: false
date: 2023-08-24
tags: ['about', 'programming']
featured_image: "images/salmon.png"
---

the website has many themes available on the sidebar dropdown menu, with both light and dark themes coming prepackaged

Instead of the theme data being in a typical format like `json`, they are actually `svg` files. This is called [the Hundred Rabbits theme system](https://github.com/hundredrabbits/Themes).

Here is an example of the sites default theme, which is `salmon.svg`
```svg
<svg width="96px" height="64px" xmlns="http://www.w3.org/2000/svg" baseProfile="full" version="1.1">
  <rect width='96' height='64' id='background' fill='#e0cdbc'></rect>
  <!-- Foreground -->
  <circle cx='24' cy='24' r='8' id='f_high' fill='#1E1D1D'></circle>
  <circle cx='40' cy='24' r='8' id='f_med' fill='#485e9b'></circle>
  <circle cx='56' cy='24' r='8' id='f_low' fill='#523d2c'></circle>
  <circle cx='72' cy='24' r='8' id='f_inv' fill='#ffffff'></circle>
  <!-- Background -->
  <circle cx='24' cy='40' r='8' id='b_high' fill='#E7D8C8'></circle>
  <circle cx='40' cy='40' r='8' id='b_med' fill='#CEC7C0'></circle>
  <circle cx='56' cy='40' r='8' id='b_low' fill='#E9E2D8'></circle>
  <circle cx='72' cy='40' r='8' id='b_inv' fill='#8c5a3d'></circle>
</svg>
```

if you want to use your own custom theme, you can make a 100R theme compliant `.svg` and drag it to anywhere on this website. Try it out with [this example](https://raw.githubusercontent.com/hundredrabbits/Themes/master/themes/boysenberry.svg) of `boysenberry.svg`

Changing themes requires javascript and is the only part of the website which uses it. If javascript is disabled, it uses `salmon.svg` as the default fallback theme
