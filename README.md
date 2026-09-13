# Gallery Menu

## Files Changed

The following files have been modified to make the gallery menu work:

* `2nd script`
* `script`
* `gallery_setup`
* `both`
* `gallery`

**To use this gallery system, you only need to replace these files in your game.**

---

## Thumbnail Images

This repository includes thumbnail images for all gallery scenes.

### Thumbnail Requirements

1. **Thumbnail size**

   The thumbnail image must have the exact dimensions defined by:

   ```python
   sx = 550
   sy = 310
   ```

   Therefore, the required thumbnail size is **550 × 310 pixels**.

2. **Hover image size**

   The hover image for the thumbnail must have the **same dimensions as the thumbnail**.

3. **Thumbnail naming**

   The thumbnail image name must match the **first image name** in the `GalleryItem` list, with `_t` added to the end.

   For example:

   ```python
   GalleryItem("Alex doggy", ["alex doggy1", "alex doggy2", "alex doggy3", "alex doggy4"])
   ```

   The first image in the list is:

   ```text
   alex doggy1
   ```

   Therefore, the thumbnail must be named:

   ```text
   alex doggy1_t
   ```

   So, the thumbnail name must always follow this format:

   ```text
   [first image name]_t
   ```

4. **Missing thumbnails**

   If you do not add a thumbnail image, Ren'Py will display an error notification instead.

5. **Using the original image instead**

   If you don't want to create thumbnail images for every scene, you can use the first image from the `GalleryItem` list as the thumbnail.

   Replace:

   ```python
   idle gallery_items[i].images[0] + "_t"
   ```

   with:

   ```python
   idle gallery_items[i].images[0]
   ```

   This will make the **first image in the gallery item's image list** appear as the thumbnail.

   **Important:** If you make this change, you also need to change the hover image size to **2560 × 1440 pixels**.
