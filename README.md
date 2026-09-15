# Gallery Menu

## Files Changed (search for "changed" word in code)

The following files have been modified to make the gallery and replay menus work:

* `2nd script`
* `script`
* `gallery_setup`
* `both`
* `gallery`
* `screens (added hide and show buttons for mobile)`
* `replay_setup`
* `replay`
  
**To use this gallery and replay  systems, you only need to replace these files in your game and update the `images` folder with the images from this repository.**

---

## How to Add Scenes to the Gallery

Add a `GalleryItem` object to the `gallery_items` list and include all CGs that belong to the scene in the `images` field.

The gallery menu uses images from the `gallery thumbnails` folder.

If you don't add a thumbnail for a scene, the gallery will automatically use the **first image** from `GalleryItem.images`.

### Thumbnail Requirements

* Size: **550 × 310**
* The thumbnail must have the **same name as the first image** in `GalleryItem.images`
* The thumbnail should be placed in the `gallery thumbnails` folder

---

## Hover Images

There are two hover images used in the gallery menu:

1. **2560 × 1440** thumbnail hover
2. **550 × 310** thumbnail hover

The hover image should be **slightly larger than the corresponding thumbnail** so that it works as a border/overlay around the image.

---

## Problems

### 1. Animated Scenes

There can be a problem when the first image of a scene is an animated image.

In this case, the gallery thumbnail will also be animated, and even after the player sees the scene in-game, it may remain **locked in the gallery**.

### Fix

Add the first image from the animated block as the first image in `GalleryItem.images`, and show that image to the player immediately before the animated scene.

For example, in `first script` there is a scene called `kim and will doggy 1`, which is animated.

The first image of this animated scene is:

```renpy
william kim doggy 1
```

So, immediately before the animated scene, add:

```renpy
scene william kim doggy 1
scene kim and will doggy 1
```

This shenanigan will **not break or visibly change the game**. Ren'Py will immediately switch from the static image to the animated one, so the player should not notice anything.

However, Ren'Py will count the static image as **seen**, allowing the corresponding gallery scene to become unlocked.

---

### 2. Thumbnail Images Appearing in the Game

There is another issue with the `gallery thumbnails` folder.

For some reason, Ren'Py can sometimes load a thumbnail image instead of the original image in the game. This seems to happen when the thumbnail and original image have the same name, especially when the original image is located inside a nested folder.

The result is usually easy to recognize: the image appears very small or only takes up a small portion of the screen.

Fix

Simply delete the problematic thumbnail from the gallery thumbnails folder.

Once the thumbnail is removed, Ren'Py will no longer be able to load it and will use the original image instead.

It is easy to identify affected images because they will appear unusually small and appear on a small portion of the screen.
