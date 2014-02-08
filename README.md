on-msa
======

#### Consent map project

The consent map project started before the hackathon. It is a structured reference database of jurisdictional privacy laws relating to notice and consent requirements. The idea is that you can look up the consent and notice laws that apply in a given context. For instance, a web plugin could deliver a set of references to laws that apply to a user when they tick the consent box on a particular website, based on the website's jurisdiction and user location.

## Crowd-sourced jurisdictional law references

In order to create the map we have crowd-sourced the references for a minimum set of common notice requirements across many jurisdictions. These include the parts of a piece of legislation that require privacy policies, terms-of-service, purpose specifications, contact details and 'Do Not Track' responses.

At present, we are working on inputting data for around a dozen jurisdictions. We have full information for Canada and the UK.

## Consent receipt

One application of the consent map is the 'consent receipt' tool; a means for a individual to get a receipt or token from a website which formally acknowledges a consent agreement between the two parties (e.g. the user stated that they have read and agreed to the privacy policy, and the website says they have received and acknowledged the users Do Not Track preference).

## API

The map is available as static dumps in CSV, JSON, XML. It will also soon be available via a RESTful API.

## Resources

Prior/related art:

- W3C: Customer experience digital data community group are defining a 'Digital datalayer'. Full spec: http://www.w3.org/2013/12/ceddl-201312.pdf or a one page summary: http://bit.ly/digitalDataSheet . This is a Javascript based standardised method of tagging the markup on a website so that it can be accessed / parsed into a tag management system, so that the data it collects is reliable and standardised. The implication for this project is that there's a privacy/security component / attribute that's assigned to each of those data values. https://www.dropbox.com/s/l352srcmz52qx6o/W3C_DataLayer_Examples.html

- Geoplugin.com/webservices/extras#eu_cookie_law This is a two part script, which allows a website to identify where the user is. Based on that, it makes a guess as to the jurisdiction, which has implications for cookie consent law requirements (i.e. explicit or implicit). It is citizen-based (IP to country). Although, it doesn't tell website what exact text they need to tell the user. That's where the consent map project could add value.

- The Schema.org microdata format has a entity called Schema.org/Organization, which reveals the company location. One option would be to hack schema.org to find out the company location and serve relevant consent map data on that basis.

## License

This data is available under CC-BY 4.0

## Creators

This is a project of;

- Kantara Consent and Information Sharing Working Group
- Open Notice
