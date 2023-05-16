# Ticket Closer

## Concepts
---
This program does very few things, so here are some concepts to understand what's going on under the hood so you can use this program better. You can skip this part if you're not interested.

### 1. Decoupling
This program is completely seperate from the Toast Android app, and it's only tool to understand what's going on is to use a screen scraper. If something goes wrong, it probably has no idea. I've implemented a few failsafes to make sure this doesn't happen, however, it's still very likely. That's why I'll recommend that only about 50-100 tickets should be closed at a time, just in case it gets out of sync.

### 2. Timing
Becuase this program is completely seperate, it has no understanding of the timing of hitting the buttons. In the Android Emulator I used to test this on my PC, I ended up just turning off animations in Android to make it faster. You can follow this guide [here](https://wccftech.com/how-to/how-to-turn-off-system-animations-on-android-tutorial) to see how. You should make sure that the timing that you choose is adequate to how the emulator / mirroring program lags behind. 

### 3. Have Fun
Sit back and watch the program do some funny goofy stuff and be happy that you don't have to do it manually.

<br>
<br>

## The Actual Guide
---
### Running the Program
This program has to be run on a PC. 

### Android Emulator / Screen Mirroring
There's two ways you can go about setting up an Android device to show on your computer screen. You can either setup an Android Emulator, or use screen mirroring. I'd recommend using screen mirroring, as installing the official Android Emulator will set you back 20-30GB of space on your computer, and can run really slow on laptops. To get started with the emulator, you can see the official guide [here](https://developer.android.com/studio/run/emulator). Once you've setup Android on the emulator, you can install the Toast APK from [toasttab.com/link/apk](http://toasttab.com/link/apk). 

Screen mirroring is, in my opinion, the better route. We'll use the open source [scrcpy](https://github.com/Genymobile/scrcpy), as it's free and it works better than any commercial product I've ever used. You'll want to use a USB connection to your PC as well. Wireless if offered, but leaves a lot of performance on the table. Go [here](https://github.com/Genymobile/scrcpy/releases/latest) to download the latest release. Grab the `scrcpy-win64-vX.X.zip` from the Assets section and extract it. Then, install the Universal ADB Drivers from [here](https://adb.clockworkmod.com/). Run scrcpy on your computer with your tablet plugged in, and it'll all come together.

### Auto vs Manual Setup
Auto setup will attempt to grab the location of the buttons based on images, and won't always work. I'd recommend giving it a shot, but in the end it doesn't save a ton of time. It will, however, add the option to use safe mode, more on that later.

Manual setup prompts you for the location of each button and stores it. Pretty easy, and has little in the way of failsafes.
