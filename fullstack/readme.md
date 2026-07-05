- Some HTML elements do not have a closing tag. These are known as void elements.
ex: `<img>` or `<img/>`
- HTML is for the content and structure. CSS is for styling. JavaScript is for adding interactivity to your web pages.
- An attribute is a value placed inside the opening tag of an HTML element. Attributes provide additional information about the element or specify how the element should behave. 
- target="_blank" enables the link to open in a new browser tab.<br>
**Attributes**<br>
- The checked attribute is used to specify that the checkbox should be checked by default. 
`<input type="checkbox" checked />`
- There are several common boolean attributes you will encounter in HTML, such as disabled, readonly, and required. These attributes are used to specify the state of an element, such as whether it is disabled, read-only, or required.
- The link element is used to link to external resources like stylesheets and site icons.<br>
`<link rel="stylesheet" href="./styles.css" />`<br>
`<link rel="icon" href="favicon.ico" />`
- UTF-8 (Unicode Transformation Format - 8-bit) is a character encoding standard that converts characters (letters, numbers, symbols, emojis, and characters from different languages) into a format that computers can store and process.
- UTF-8 encoding, ensuring that all characters are displayed correctly.
- The div element is used as a container to group other elements.
- The section element has semantic meaning over the div element which is not semantic.
- The id attribute adds a unique identifier to an HTML element.
- In contrast to the id attribute, the class attribute value does not need to be unique and can contain spaces.
- If you wanted to add multiple class names to an element, you can do so by separating the names by a space. 
- when should you use an id versus a class? Classes are best used when you want to apply a set of styles to many elements. If you want to target a specific element, it is best to use id because those values need to be unique.<br>
**HTML Entities** <br>
- to display the text This is an <img/> element on the screen. If you use the code currently in the editor, it won't display the desired result.<br>
ex:&lt;p&gt;learning is fun&lt;/p&gt;
- These types of character references are known as named character references. Named references start with an ampersand sign (&) and end with a semicolon (;). By using a named character reference, the HTML parser will not confuse this with an actual HTML element.
- Another type of character reference would be the decimal numeric reference. This character reference starts with an ampersand sign and hash symbol (#), followed by one or more decimal digits, followed by a semicolon.<br>
You can use &#169; for the copyright symbol and &#174; for the registered trademark symbol.
- The last type of character reference would be the hexadecimal numeric reference. This character reference starts with an ampersand sign, hash symbol, and the letter x. Then it is followed by one or more ASCII hex digits and ends with a semicolon.
- You can use &#x20AC; for the euro symbol and &#x03A9; for the Greek capital letter Omega symbol.
- The audio and video elements allow you to add sound and video content to your HTML documents.<br>
  Example: `<audio src="https://cdn.freecodecamp.org/curriculum/js-music-player/cruising-for-a-musing.mp3 controls"></audio>`
- there are several other attributes that enhance the functionality of the audio element. The loop attribute is a boolean attribute that makes the audio replay continuously.
- Another attribute you can use is the muted attribute. When present in the audio element, this boolean attribute will start the audio in a muted state. 
- All the attributes we have learned so far are also supported in the video element. Here's an example of using a video element with the loop, controls, and muted attributes.
- Add the autoplay attribute to the opening video tag so the video plays automatically.
- The width attribute is being used here to make the video smaller and fit better in the preview window.<br>

Example: `<video src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4" loop controls muted width="400"></video>`
- MIME (Multipurpose Internet Mail Extensions) is a standard to describe documents in other forms besides ASCII text, for example, audio, video, and images. MP4, formally known as MPEG-4 Part 14, is a digital multimedia container format. It is widely used for storing video and audio, but it can also include other data types like subtitles and still images. MP4 files are designed for streaming over the Internet and are compatible with many devices and platforms.
- Another common MIME type is the video/webm MIME type. WebM is an open-source audiovisual media file format developed by Google, primarily designed for web-based media content. It supports video codecs like VP8, VP9, and AV1, and audio codecs such as Vorbis and Opus, making it a popular choice for HTML5 video and audio elements.
- If you wanted to display an image while the video is downloading, you can use the poster attribute. 
- Another common MIME type is the video/ogg MIME type.Ogg is a digital multimedia container format designed to provide for efficient streaming and manipulation of digital multimedia. It is maintained by the Xiph.Org Foundation and is free and open, unrestricted by software patents. Its name is derived from "ogging", jargon from the computer game Netrek.
- video/quicktime MIME type. QuickTime is an extensible multimedia architecture created by Apple, which supports playing, streaming, encoding, and transcoding a variety of digital media formats. Not as popular as the MP4 format, you may need it for legacy application support.