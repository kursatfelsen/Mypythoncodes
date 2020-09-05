from selenium import webdriver

import time

browser = webdriver.Firefox()

url = "https://cwrdistribution.com/b2b/product/57364/scotty-327-fender-ring-2-pack"

browser.get(url)

#time.sleep(3)

username = browser.find_element_by_css_selector(".email")

password = browser.find_element_by_css_selector(".password")

login = browser.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.no-mobile.no-phone.no-tablet.mobilegradea body.not-logged-in div.container-fluid.noPrint.padding-nav-offset main.container.noPrint div.panel.panel-smart.panel-login2 div.panel-body.row.justify-content-center form.login-form.col-xs-12.col-sm-8.col-lg-6 div.text-center button.btn.btn-primary")

username.send_keys("therebellineonline@gmail.com")

password.send_keys("Rebel2020!")

html_part1 = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="https://www.w3.org/1999/xhtml"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"/><link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700" rel="stylesheet"><link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet"><meta name="description" content="The Rebel Line eBay Store - Proffetional eBay Template Design Solution - fiverr/merkrv or merkrv"><meta name="keywords" content="ebay , ebay template, listing tempalte , ebay template generator, ebay template design, ebay templates uk, ebay templates html, ebay template software, ebay templates shop, ebay template editor, ebay template listing, ebay template free, ebay template shop, ebay template download, ebay template responsive, ebay template builder free, ebay template active content, ebay template auction, ebay template auctiva, ebay templates australia, "><meta name="author" content="merkrv - merkrv - fiverr/merkrv"><title>The Rebel Line eBay Store</title><link rel="stylesheet" href="https://merkrv.com/ebay/TheRebelLine/SC/styles4.css" type="text/css"></head><body><div><div class="topbannerupup"><div class="topbannerup"><div class="topbanner"><img src="https://merkrv.com/ebay/TheRebelLine/PIC/topbanner.png"></div></div></div><div class="topbanner2up"><div class="topbanner2"><p class="p1">Any change in the value of Dollar will Reflect a Price Change of Future Stock</p><p class="p2">so purchase today !</p></div></div><!--CONTENT S--><div class="contentup"><div class="content"><div class="main"><img src="""
html_part2 = '"https://merkrv.com/ebay/PIC/sample-image2.jpg"'

html_part3 = """></div><div class="banner3_5"><div class="banner3_5_dv1"><p>PRODUCT INFORMATION</p></div><div class="banner3_5_dv2"><h1 class="ttl">"""

html_part4 = """Add your product title here"""

html_part5 = """</h1><p>"""

html_part6 = """Add your product description here"""

html_part7 = """</p><p id="innerttl">Features</p><ul><li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li></ul></div></div><div class="banner4"><div class="banner4_dv2"><div class="banner4_dv1"><p>Specifications</p></div><ul><li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li></ul></div><div class="banner4_dv3"><div class="banner4_dv1"><p>Package Content</p></div><ul><li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li>
<li>Add_Your_Text_Here</li></ul></div></div><div class="banner3"><div class="banner3_dv1"><p>PRODUCT IMAGES</p></div><div class="banner3_dv2"><div class="leftdv"><div class="imgwrap"><span class="helper"></span><img id="left" src="https://merkrv.com/ebay/PIC/sample-image.jpg" alt=""></div><div class="leftdvinner"><div><h2>Product_Feature</h2></div></div></div></div></div><div class="banner2"><div class="banner2_dv1"><p>WHY BUY FROM US?</p><div><img class="why_img" src="https://merkrv.com/ebay/TheRebelLine/PIC/why.png"></div></div><div class="banner2_dv2"><div class="banner2_dv2_1"><div class="banner2_dv2_2"><p>LATEST PRODUCT REVIEWS<a target="_blank" href="https://feedback.ebay.com/ws/eBayISAPI.dll?ViewFeedback2&userid=therebelline&ftab=AllFeedback&myworld=true&rt=nc&_trksid=p2050430.m2531.l4585" id="feedback_button">View All Reviews</a></p></div><div class="banner2_dv2_3"><p class="pp1">Thank you so much!</p><p class="pp2">Buyer: c***p (866) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Thank you! Fast shipping</p><p class="pp2">Buyer: m***l (474) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Great seller!! Item as described.</p><p class="pp2">Buyer: 1***5 (183) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Repeat customer , great eBay seller ! Fast shipping!</p><p class="pp2">Buyer: y***y (837) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Great product , fast delivery , great customer service !</p><p class="pp2">Buyer: y***y (837) : <em>During past month</em></p></div></div></div></div><div class="banner5up"><div class="banner5_dv1up"><div class="banner5_dv1"><p>POLICIES INFORMATION</p></div></div><div class="banner5"><div class="banner5_dv2"><div><p class="payment">PAYMENT</p></div></div><div class="banner5_dv3"><div><p class="p2">We require that all payments be paid through PayPal. Your address must be confirmed. Buyers who pay with unconfirmed addresses will not be accepted.</p></div></div><div class="banner5_dv2"><div><p class="shipping">Shipping & Handling</p></div></div><div class="banner5_dv3"><div><p class="p2"> We're shipping the item by UPS Ground, USPS, FedEx smart post, packing and handling time is 1 business day and it would extend if there is weekend or holiday.<br /><br /> We also offer expedited shipping at an extra cost.<br /><br /> Item purchased is shipped from West or East Coast Warehouses depending on availability.<br /><br /> PO Box shipments are limited and have additional shipping costs. Please be sure a physical address is available for shipping in Paypal and eBay. If a PO Box is the only shipping option please contact us for a quote on additional shipping costs. If you make a purchase and a PO Box is the only address provided you will be contacted to make arrangements to cover additional shipping costs.<br /><br /> A shipping surcharge applies to shipments to Alaska and Hawaii. The surcharge amount is dependent on the size, weight and cost of the item and will be included in your total at checkout. Shipping time is 7-21 days<br /><br /> We don't ship to APO/FPO boxes.<br /><br /> We use Ebay's Global Shipping Program. Ebay will automatically charge you the International shipping and will take responsibility for the International Shipment.<br /><br /> Shipping charges are non-refundable.</p></div></div><div class="banner5_dv2"><div><p class="returns">Returns</p></div></div><div class="banner5_dv3"><div><p class="p2"> Per our return policy the item can be returned in 30 days, buyer is responsible for the return shipping, 20% restocking fee may apply.<br /><br /> ALL ITEMS MUST BE RETURNED UNUSED IN ORIGINAL PACKAGING<br /><br /> All items are shipped from our distributor new in the original packaging. Please contact us by email in the event that your item arrives with damage. We can replace the item right away with pictures of the damage. Please do not use the Ebay Return Service as you will most likely not be returning your item. If you just email us, we can have a replacement or refund right out to you! We don't use the return service as we have our own replacement/refund service that is easier, better and faster.</p></div></div><div class="banner5_dv2"><div><p class="feedback">FEEDBACK</p></div></div><div class="banner5_dv3"><div><p class="p2">Our goal is always 100% complete customer satisfaction. If for any reason you are not satisfied please contact us before leaving feedback. We strive for 100% satisfied loyal customers who are happy to shop with us again.<br /><br /> Shop With Confidence.</p></div></div><div class="banner5_dv2"><div><p class="about">About Us</p></div></div><div class="banner5_dv3"><div><p class="p2">We strive to accommodate buyers with the large selections of unique and high quality products at fair price and ultimate service. We are committed to excellence and always strive to improve the experience of our customers.<br /><br /> Please contact us with any questions, comments or concerns.</p></div></div></div></div></div></div><div class="clear"></div><!--MIDDLE E--></div></div><!--CONTENT E--></div><!--MAIN E--><div class="banner6up"><div class="banner6"><div class="banner6_dv4"><div class="banner6_dv4_1"><img src="https://merkrv.com/ebay/TheRebelLine/PIC/logo.png"></div><div class="banner6_dv4_2"><p>ANY QUESTIONS? ASK US<br><span>We happily respond within 24hrs</span></p></div><div class="banner6_dv4_3"><div class="banner6_dv4_3_se1"><span class="line1">Dedicated To</span><span class="line2">Five Star</span><span class="line3">Customer Support</span><span class="line4"></span></div><div class="banner6_dv4_3_se2"><img src="https://merkrv.com/ebay/TheRebelLine/PIC/lady.png"></div></div></div></div><div class="banner6_dv5up"><div class="banner6_dv5"><a target="_blank" href="https://my.ebay.com/ws/eBayISAPI.dll?AcceptSavedSeller&linkname=includefavoritestore&sellerid=therebelline" id="a1">Add Us to Favorite Seller</a><span id="a2">2020 Copyright The Rebel Line. All Rights Reserved : <span>Powered by MerkRv</span><img src="https://merkrv.com/ebay/TheRebelLine/PIC/logomerk.png"></span></div></div></div><div class="footer_space"></div></body></html>
"""

login.click()


time.sleep(2)

"""
data = browser.find_elements_by_css_selector(".content")
"""

"""
for element in data:
	print(element.get_attribute('innerHTML'))
"""

html_list = browser.find_element_by_id("description")
items = html_list.find_elements_by_tag_name("p")
description = ""
isitTrue = False
print(len(items))
for item in items:
    text = item.get_attribute('innerHTML')
    print(text)
    if (len(text)>10):
    	if isitTrue:
    		text = "<br><br>" +text
    	isitTrue = True
    if not ("WARNING" in text) and len(text)>10 and not ("Features" in text):
    	description += text

html_part6 = description
"""

html_list = browser.find_element_by_id("description")
items = html_list.find_elements_by_tag_name("p")
description = ""

isitTrue = False
for item in items:
    text = item.text
    if (len(text)>15):
    	if isitTrue:
    		text = "<br><br>" +text
    	isitTrue = True
    	print (text)
    if not ("WARNING" in text) and len(text)>15:
    	description += text

html_part6 = description
"""

"""
try:
	description = browser.find_element_by_css_selector("#description > div:nth-child(1) > p:nth-child(1)")
	html_part6 = description.get_attribute('innerHTML')
except:
	html_part6 = ""

"""

html_source = browser.page_source


if "WARNING" in html_source:
	warning = browser.find_element_by_xpath("//*[contains(text(), 'This product can expose')]")
	html_part7 = """</p><p id="innerttl">Warning</p><ul>"""	
	html_part8 = warning.text[8:]
	html_part9 = """</ul></div></div><div class="banner4"><div class="banner4_dv2"><div class="banner4_dv1"><p>"""
else:
	html_part7 = """</p><p id="innerttl"></p><ul>"""
	html_part8 = "</ul>" 
	html_part9 = """</div></div><div class="banner4"><div class="banner4_dv2"><div class="banner4_dv1"><p>"""

title = browser.find_element_by_css_selector(".page-title")

lis = browser.find_elements_by_css_selector(".p.li")

time.sleep(2)

elements = browser.find_elements_by_xpath("/html/body/div[4]/main/div[3]/div/div/div[2]/div/div[1]/div/ul")



if len(elements)>=1:
	html_part10 = """Features</p></div><ul>"""
	liste = (elements[0].text).split("\n")
	reliste= []
	for element in liste:
		reliste.append("<li> "+element+" </li>")
	html_part11= ""
	for element in reliste:
		html_part11+=element
	html_part12 = """</ul></div><div class="banner4_dv3"><div class="banner4_dv1"><p>Package Content</p></div><ul><li>"""
	html_part13 = "1 x "+title.text
	html_part14 = """</li>
	</ul></div></div><div class="banner3"><div class="banner3_dv1"><p>PRODUCT IMAGES</p></div><div class="banner3_dv2"></div></div><div class="banner2"><div class="banner2_dv1"><p>WHY BUY FROM US?</p><div><img class="why_img" src="https://merkrv.com/ebay/TheRebelLine/PIC/why.png"></div></div><div class="banner2_dv2"><div class="banner2_dv2_1"><div class="banner2_dv2_2"><p>LATEST PRODUCT REVIEWS<a target="_blank" href="https://feedback.ebay.com/ws/eBayISAPI.dll?ViewFeedback2&userid=therebelline&ftab=AllFeedback&myworld=true&rt=nc&_trksid=p2050430.m2531.l4585" id="feedback_button">View All Reviews</a></p></div><div class="banner2_dv2_3"><p class="pp1">Thank you so much!</p><p class="pp2">Buyer: c***p (866) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Thank you! Fast shipping</p><p class="pp2">Buyer: m***l (474) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Great seller!! Item as described.</p><p class="pp2">Buyer: 1***5 (183) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Repeat customer , great eBay seller ! Fast shipping!</p><p class="pp2">Buyer: y***y (837) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Great product , fast delivery , great customer service !</p><p class="pp2">Buyer: y***y (837) : <em>During past month</em></p></div></div></div></div><div class="banner5up"><div class="banner5_dv1up"><div class="banner5_dv1"><p>POLICIES INFORMATION</p></div></div><div class="banner5"><div class="banner5_dv2"><div><p class="payment">PAYMENT</p></div></div><div class="banner5_dv3"><div><p class="p2">We require that all payments be paid through PayPal. Your address must be confirmed. Buyers who pay with unconfirmed addresses will not be accepted.</p></div></div><div class="banner5_dv2"><div><p class="shipping">Shipping & Handling</p></div></div><div class="banner5_dv3"><div><p class="p2"> We're shipping the item by UPS Ground, USPS, FedEx smart post, packing and handling time is 1 business day and it would extend if there is weekend or holiday.<br /><br /> We also offer expedited shipping at an extra cost.<br /><br /> Item purchased is shipped from West or East Coast Warehouses depending on availability.<br /><br /> PO Box shipments are limited and have additional shipping costs. Please be sure a physical address is available for shipping in Paypal and eBay. If a PO Box is the only shipping option please contact us for a quote on additional shipping costs. If you make a purchase and a PO Box is the only address provided you will be contacted to make arrangements to cover additional shipping costs.<br /><br /> A shipping surcharge applies to shipments to Alaska and Hawaii. The surcharge amount is dependent on the size, weight and cost of the item and will be included in your total at checkout. Shipping time is 7-21 days<br /><br /> We don't ship to APO/FPO boxes.<br /><br /> We use Ebay's Global Shipping Program. Ebay will automatically charge you the International shipping and will take responsibility for the International Shipment.<br /><br /> Shipping charges are non-refundable.</p></div></div><div class="banner5_dv2"><div><p class="returns">Returns</p></div></div><div class="banner5_dv3"><div><p class="p2"> Per our return policy the item can be returned in 30 days, buyer is responsible for the return shipping, 20% restocking fee may apply.<br /><br /> ALL ITEMS MUST BE RETURNED UNUSED IN ORIGINAL PACKAGING<br /><br /> All items are shipped from our distributor new in the original packaging. Please contact us by email in the event that your item arrives with damage. We can replace the item right away with pictures of the damage. Please do not use the Ebay Return Service as you will most likely not be returning your item. If you just email us, we can have a replacement or refund right out to you! We don't use the return service as we have our own replacement/refund service that is easier, better and faster.</p></div></div><div class="banner5_dv2"><div><p class="feedback">FEEDBACK</p></div></div><div class="banner5_dv3"><div><p class="p2">Our goal is always 100% complete customer satisfaction. If for any reason you are not satisfied please contact us before leaving feedback. We strive for 100% satisfied loyal customers who are happy to shop with us again.<br /><br /> Shop With Confidence.</p></div></div><div class="banner5_dv2"><div><p class="about">About Us</p></div></div><div class="banner5_dv3"><div><p class="p2">We strive to accommodate buyers with the large selections of unique and high quality products at fair price and ultimate service. We are committed to excellence and always strive to improve the experience of our customers.<br /><br /> Please contact us with any questions, comments or concerns.</p></div></div></div></div></div></div><div class="clear"></div><!--MIDDLE E--></div></div><!--CONTENT E--></div><!--MAIN E--><div class="banner6up"><div class="banner6"><div class="banner6_dv4"><div class="banner6_dv4_1"><img src="https://merkrv.com/ebay/TheRebelLine/PIC/logo.png"></div><div class="banner6_dv4_2"><p>ANY QUESTIONS? ASK US<br><span>We happily respond within 24hrs</span></p></div><div class="banner6_dv4_3"><div class="banner6_dv4_3_se1"><span class="line1">Dedicated To</span><span class="line2">Five Star</span><span class="line3">Customer Support</span><span class="line4"></span></div><div class="banner6_dv4_3_se2"><img src="https://merkrv.com/ebay/TheRebelLine/PIC/lady.png"></div></div></div></div><div class="banner6_dv5up"><div class="banner6_dv5"><a target="_blank" href="https://my.ebay.com/ws/eBayISAPI.dll?AcceptSavedSeller&linkname=includefavoritestore&sellerid=therebelline" id="a1">Add Us to Favorite Seller</a><span id="a2">2020 Copyright The Rebel Line. All Rights Reserved : <span>Powered by MerkRv</span><img src="https://merkrv.com/ebay/TheRebelLine/PIC/logomerk.png"></span></div></div></div><div class="footer_space"></div></body></html>"""
	html = html_part5 + html_part6 + html_part7 + html_part8 + html_part9 + html_part10 + html_part11 + html_part12 + html_part13 + html_part14 
else:
	html_part10 = """Package Content</p></div><ul><li>"""
	html_part11 = "1 x " + title.text
	html_part12 = """</li></ul></div><div class="banner4_dv3"><div class="banner4_dv1"><p></p></div><ul></ul></div></div><div class="banner3"><div class="banner3_dv1"><p>PRODUCT IMAGES</p></div><div class="banner3_dv2"></div></div><div class="banner2"><div class="banner2_dv1"><p>WHY BUY FROM US?</p><div><img class="why_img" src="https://merkrv.com/ebay/TheRebelLine/PIC/why.png"></div></div><div class="banner2_dv2"><div class="banner2_dv2_1"><div class="banner2_dv2_2"><p>LATEST PRODUCT REVIEWS<a target="_blank" href="https://feedback.ebay.com/ws/eBayISAPI.dll?ViewFeedback2&userid=therebelline&ftab=AllFeedback&myworld=true&rt=nc&_trksid=p2050430.m2531.l4585" id="feedback_button">View All Reviews</a></p></div><div class="banner2_dv2_3"><p class="pp1">Thank you so much!</p><p class="pp2">Buyer: c***p (866) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Thank you! Fast shipping</p><p class="pp2">Buyer: m***l (474) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Great seller!! Item as described.</p><p class="pp2">Buyer: 1***5 (183) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Repeat customer , great eBay seller ! Fast shipping!</p><p class="pp2">Buyer: y***y (837) : <em>During past month</em></p></div><div class="banner2_dv2_3"><p class="pp1">Great product , fast delivery , great customer service !</p><p class="pp2">Buyer: y***y (837) : <em>During past month</em></p></div></div></div></div><div class="banner5up"><div class="banner5_dv1up"><div class="banner5_dv1"><p>POLICIES INFORMATION</p></div></div><div class="banner5"><div class="banner5_dv2"><div><p class="payment">PAYMENT</p></div></div><div class="banner5_dv3"><div><p class="p2">We require that all payments be paid through PayPal. Your address must be confirmed. Buyers who pay with unconfirmed addresses will not be accepted.</p></div></div><div class="banner5_dv2"><div><p class="shipping">Shipping & Handling</p></div></div><div class="banner5_dv3"><div><p class="p2"> We're shipping the item by UPS Ground, USPS, FedEx smart post, packing and handling time is 1 business day and it would extend if there is weekend or holiday.<br /><br /> We also offer expedited shipping at an extra cost.<br /><br /> Item purchased is shipped from West or East Coast Warehouses depending on availability.<br /><br /> PO Box shipments are limited and have additional shipping costs. Please be sure a physical address is available for shipping in Paypal and eBay. If a PO Box is the only shipping option please contact us for a quote on additional shipping costs. If you make a purchase and a PO Box is the only address provided you will be contacted to make arrangements to cover additional shipping costs.<br /><br /> A shipping surcharge applies to shipments to Alaska and Hawaii. The surcharge amount is dependent on the size, weight and cost of the item and will be included in your total at checkout. Shipping time is 7-21 days<br /><br /> We don't ship to APO/FPO boxes.<br /><br /> We use Ebay's Global Shipping Program. Ebay will automatically charge you the International shipping and will take responsibility for the International Shipment.<br /><br /> Shipping charges are non-refundable.</p></div></div><div class="banner5_dv2"><div><p class="returns">Returns</p></div></div><div class="banner5_dv3"><div><p class="p2"> Per our return policy the item can be returned in 30 days, buyer is responsible for the return shipping, 20% restocking fee may apply.<br /><br /> ALL ITEMS MUST BE RETURNED UNUSED IN ORIGINAL PACKAGING<br /><br /> All items are shipped from our distributor new in the original packaging. Please contact us by email in the event that your item arrives with damage. We can replace the item right away with pictures of the damage. Please do not use the Ebay Return Service as you will most likely not be returning your item. If you just email us, we can have a replacement or refund right out to you! We don't use the return service as we have our own replacement/refund service that is easier, better and faster.</p></div></div><div class="banner5_dv2"><div><p class="feedback">FEEDBACK</p></div></div><div class="banner5_dv3"><div><p class="p2">Our goal is always 100% complete customer satisfaction. If for any reason you are not satisfied please contact us before leaving feedback. We strive for 100% satisfied loyal customers who are happy to shop with us again.<br /><br /> Shop With Confidence.</p></div></div><div class="banner5_dv2"><div><p class="about">About Us</p></div></div><div class="banner5_dv3"><div><p class="p2">We strive to accommodate buyers with the large selections of unique and high quality products at fair price and ultimate service. We are committed to excellence and always strive to improve the experience of our customers.<br /><br /> Please contact us with any questions, comments or concerns.</p></div></div></div></div></div></div><div class="clear"></div><!--MIDDLE E--></div></div><!--CONTENT E--></div><!--MAIN E--><div class="banner6up"><div class="banner6"><div class="banner6_dv4"><div class="banner6_dv4_1"><img src="https://merkrv.com/ebay/TheRebelLine/PIC/logo.png"></div><div class="banner6_dv4_2"><p>ANY QUESTIONS? ASK US<br><span>We happily respond within 24hrs</span></p></div><div class="banner6_dv4_3"><div class="banner6_dv4_3_se1"><span class="line1">Dedicated To</span><span class="line2">Five Star</span><span class="line3">Customer Support</span><span class="line4"></span></div><div class="banner6_dv4_3_se2"><img src="https://merkrv.com/ebay/TheRebelLine/PIC/lady.png"></div></div></div></div><div class="banner6_dv5up"><div class="banner6_dv5"><a target="_blank" href="https://my.ebay.com/ws/eBayISAPI.dll?AcceptSavedSeller&linkname=includefavoritestore&sellerid=therebelline" id="a1">Add Us to Favorite Seller</a><span id="a2">2020 Copyright The Rebel Line. All Rights Reserved : <span>Powered by MerkRv</span><img src="https://merkrv.com/ebay/TheRebelLine/PIC/logomerk.png"></span></div></div></div><div class="footer_space"></div></body></html>"""
	html = html_part5 + html_part6 + html_part7 + html_part8 + html_part9 + html_part10 + html_part11 + html_part12



photo = browser.find_element_by_css_selector(".img-fluid")

photo.click()

"""
time.sleep(2)
"""
try:
	jpg = browser.find_element_by_css_selector(".featherlight-image").get_attribute("src")
except:
	time.sleep(2)
	jpg = browser.find_element_by_css_selector(".featherlight-image").get_attribute("src")

html_part2 = jpg

html_part4 = title.text
print(html_part1 + html_part2 + html_part3+html_part4)
print(html)

result_html = html_part1 + html_part2 + html_part3 + html_part4 + html

browser.close()
