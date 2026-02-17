# GSoC14_email

::: {#content dir="ltr" lang="en"}
# Ideas for a RFC 6532 API {#Ideas_for_a_RFC_6532_API}

## Policy {#Policy}

- \- the internal charset has to be changeable (or at least a USASCII/UTF8 switch is needed)

## Header {#Header}

### \_header_value_parser {#A_header_value_parser}

- \- use settings from policy in \_fold

## Steps {#Steps}

1.  change the Header class in header.py to make the default charset changeable (add \'\_internal_charset\' property)

2.  NOT SURE ABOUT THIS: create new classes in the headerregistry.py (e.g. [UnicodeAddressHeader](./UnicodeAddressHeader.html){.nonexistent} as inheritor of [AddressHeader](./AddressHeader.html){.nonexistent}

3.  provide an alternative header map (e.g. \_unicode_header_map) using the new classes

4.  [HeaderRegistry](./HeaderRegistry.html){.nonexistent}: create an inherited class with the \_unicode_header_map as default.

\...

1.  create a policy making use of the above
:::
