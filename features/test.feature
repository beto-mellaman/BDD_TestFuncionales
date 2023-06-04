Feature: testing browser title

Scenario Outline: visit "<browser page>" and check "<browser title>"
    When we visit "<browser page>"
    Then it should have a title "<browser title>"

    Examples: Browser
        | browser page                     | browser title |
        | https://www.lidl.es              | Compra Online \| Lidl |


Scenario Outline: search "<product>" and count "<total>"
    When we search "<product>"
    Then it should be "<total>"

    Examples: Browser
        | product       | total |
        | wifi          | 7     |

Scenario Outline: after search "wifi" check web "<title>"
    Then web should have a title "<title>"

    Examples:
        | title |
        | Resultado de búsqueda \| Lidl |

Scenario Outline: after search "wifi" check search "<searchTitle>"
    Then search title should be a title "<searchTitle>"

    Examples:
        | searchTitle |
        | 7 productos |

Scenario Outline: add "product" to "shoping cart" and chek "<message>"
    When add product
    Then check "<message>"

    Examples:
        | message |
        | ¡Buena elección! El artículo ha sido añadido a tu cesta de la compra. |

