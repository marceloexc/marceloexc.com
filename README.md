# marceloexc.com
My personal website made in Hugo

## Dependencies

* Hugo Extended Version (0.10X)

* Python and BeautifulSoup4 (for `nutrition-facts` shortcode size calculations)

## Building

1. Build the site

```
hugo
```

2. Run BS4 command for size calculation from [LowTechMagazine](https://github.com/lowtechmag/solar_v2)

```
python3 utils/calculate_size.py --directory public/ --baseURL http://marceloexc.com
```
