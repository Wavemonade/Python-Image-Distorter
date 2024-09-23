# Python Image Distorter
A simple python program for simple image effects

![Image Distorter Img](https://github.com/user-attachments/assets/9bbeb36f-e266-4295-99ad-a463586b06c5)

## How to use it
1. Run the `ImageDistorted.py` file (e.g.: running it through the python console or code editors like Visual Studio Code)
2. Pick an Image with the `Change Directory` Button
3. Add one or more of the Effects to the image
   - This can take a long time, especially for larger images because it is currently done on the cpu and without threading
   - Some Effects (like the Gradient Creators, `GaussianBlurSubract` and the Scanlines) need the console for input (e.g.: the pixel width for scanlines, how big the Gaussian Blur should be (in Pixels), e.t.c)
4. Export the Image using the `Export Image` Button. The Image will be exported in the `Exports` folder where the Python programm is saved

### Heres how it would look like with the `MeltDown` effect
![Image Distorter Img 2](https://github.com/user-attachments/assets/44f94972-793c-466e-ba45-0ae911b6e03a)


## Future Plans
- [ ] More modular programming (so it is easier to add Effects (currently you need to put the effect in the `Effects` folder and reference it in the `EffectsFinder.py`
- [ ] Making the programm more bug-proof
- [ ] Faster Image processing
- [ ] Better Layout and Design
