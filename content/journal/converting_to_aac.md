---
title: "Converting my .mp3 collection to AAC"
draft: true
date: 2024-04-10T22:09:05-05:00
blog: false
tags: ["website"]
featured_image: ""
description: "Born to use OPUS, forced to use AAC"
toc: false
---

### HEARTBREAKING: Not All Music Is On Streaming

My Apple Music subscription comes with something called "Cloud Library" - a feature that lets me mix both streamed and local music together, add them to the same playlists, play them on any AirPlay device, etc. This comes in handy because some of my favorite music is *not* on streaming (e.g., the [best EDM album](https://rateyourmusic.com/release/album/leroy/grave-robbing/), the[ best post-rock live album](https://rateyourmusic.com/release/unauth/godspeed-you-black-emperor/05_14_03-nantes-france/), the [best screamo album](https://rateyourmusic.com/release/album/corea/los-peores-7-km-de-mi-vida/), I can go on and on). This means that my collection of local albums on my computer keeps growing

However, I am _not_ an audiophile! Having a .FLAC-based collection is so many gigabytes (plus, FLAC's can't even have an ID3-embedded image in its metadata, meaning that you will always have to have a `cover.jpg` in the album directory). Instead, I value having good-enough sounding music that will take up less space locally.

Normally this would mean just using .MP3's as they are the most common, but the format is quite old and the compression algorithm is also outdated. My measly 256GB Laptop needs something with a more effective compression

### Why AAC?

It's because of Apple Music. With the Mac client, the only formats that it accepts (afaik) are `.mp3`, `.m4a` (AAC), and `.wav`. Pretty sure it doesn't even support `.flac`. 

Maybe in the future I will completely hop off the streaming ship and go self-hosted with my Jellyfin setup, as it seems that `OPUS` compression is way better. However, `AAC` does produce a ~20% smaller filesize to comparable `MP3`'s, which is good enough for me right now

### What you'll need

The prerequisites for this are:

1. `FFmpeg` with the `libfdk_aac` library. This will do the actual converting for us. This does not come by default in the regular `FFmpeg` installs, and I had to let Homebrew build a version of it for me with the library enabled. I did this by uninstalling the version that I already had and running
```
brew install homebrew-ffmpeg/ffmpeg/ffmpeg --with-fdk-aac --HEAD
```

2. [AtomicParsley](https://github.com/wez/atomicparsley), which will just handle the cover art. On Mac, It's just:
```
brew install atomicparsley
```


### How I do it


```
find . -type f -name "*.flac" -exec sh -c 'ffmpeg -i "$1" -c:a libfdk_aac -b:a 256k -vn -c:s:0 copy -metadata:s:s:0 language=eng "./$(basename "$1" .flac).m4a"' _ {} \;
```

and then to get the actual album cover art, there should be a cover.jpg in there somewhere... 

```
for i in *.m4a; AtomicParsley $i --artwork Cover.jpg --overWrite; end;
```


