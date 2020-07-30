# Testing

 In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

 Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

 For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

 1. Contact form:
     1. Go to the "Contact Us" page
     2. Try to submit the empty form and verify that an error message about the required fields appears
     3. Try to submit the form with an invalid email address and verify that a relevant error message appears
     4. Try to submit the form with all inputs valid and verify that a success message appears.

 In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

 You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

### Validation

#### HTML
I validated the HTML with the [W3 Validation Service](https://validator.w3.org/). It picked up a couple of stray closing tags I missed like `</i>`, and warned I need not use the type="text" attribute for javascripts.

#### CSS

I validated the CSS with the [W3 CSS Validation Service](http://www.css-validator.org/) for CSS Level 3 and no errors were found.

#### Javascript



### Testing on Browsers, Screen sizes and Devices
I tested the website on the following browsers and devices:
- Chrome on PC and Mac
- Firefox on PC and Mac
- Safari on Mac
- Microsoft Edge V44
- Microsoft Internet Explorer V11
- Chrome on Samsung Galaxy S8, Android V9
- Firefox on Samsung Galaxy S8
- Native Browser on Samsung Galaxy S8
- Chrome on Lenovo 10" Tablet, Android V6

When I deployed the site to Github Pages and tested on an Android mobile the Get weather for another city function would not work. This worked fine on my localhost on computer, so I connected my Android phone to my desktop to do remote debugging, following [Google's instruction](https://developers.google.com/web/tools/chrome-devtools/remote-debugging). Then I could use my Dev Tools console and coud see the browser error. It was telling me that mixed content was loaded over HTTPS and that the XMLHttpRequest was blocked because it was bein requested over http. So I just had to check my writeToDocument function and change the API URL to use HTTPS. My localhost was not using https so I did not see this error until this point.

I also realised it would be easier to develop locally and view the localhost site on my Android phone. I was able to set this up through Chrome Dev tools, again following [Google's instruction](https://developers.google.com/web/tools/chrome-devtools/remote-debugging/local-server).

Testing other devices - I ran the website through [Browser Stack](https://www.browserstack.com/) on a free account to test on real devices and screen sizes. I was able to live test the following devices:
 - Samsung Galaxy Tab, Chrome, 4, 10.1 in - 5.4 x 8.6in, Resolution 1280 x 800px
 - iPhone 6S, Safari, 4.7 in - 2.3 x 4.1 in, Resolution 750 x 1334px, Viewport 375 x 667 dp
 - iPad Air 2, iOS v8, Safari, Resolution 9.7 in - 5.8 x 7.8in, Viewport 768 x 1024 dp
 
They worked fine apart from iPad Air 2, which seemed to break the Bootstrap grid. Some research indicated that the CSS flex property was not supported on iOS v8. Considering iOS 8 was out in 2014, this is probably not much of an issue now. Apple would usually push updated to devices over the years. Ref - https://github.com/twbs/bootstrap/issues/24012