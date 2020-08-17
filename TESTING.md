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

### Colour Constrast Checking
I used [WebAIM's](https://webaim.org/resources/contrastchecker/) contrast checker to ensure that text on coloured backgrounds is readable and to WCAG AA Standard, especially white text on coloured backgrounds.

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


Testing other devices - I ran the website through [Browser Stack](https://www.browserstack.com/) on a free account to test on real devices and screen sizes. I was able to live test the following devices:
 - Samsung Galaxy Tab, Chrome, 4, 10.1 in - 5.4 x 8.6in, Resolution 1280 x 800px
 - iPhone 6S, Safari, 4.7 in - 2.3 x 4.1 in, Resolution 750 x 1334px, Viewport 375 x 667 dp
 - iPad Air 2, iOS v8, Safari, Resolution 9.7 in - 5.8 x 7.8in, Viewport 768 x 1024 dp
 
