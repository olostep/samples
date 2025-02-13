## URL: https://docs.stripe.com/payments/checkout/upsells

 Subscription upsells | Stripe Documentation     

[Skip to content](#main-content)

Configure subscription upsells

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fupsells)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fupsells)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Add discounts](/payments/checkout/discounts)

Configure subscription upsells

[Configure cross-sells](/payments/checkout/cross-sells)

[Let customers complete orders for free](/payments/checkout/no-cost-orders)

[Display yearly prices in monthly terms](/payments/checkout/yearly-price-display)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Add discounts, upsells, and cross-sells](/payments/checkout/promotions "Add discounts, upsells, and cross-sells")

Subscription upsells
====================

Enable customers to upgrade their subscription plan at checkout by using upsells.
---------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Subscription upsells give customers the option to upgrade to a longer-term plan using Checkout. Upselling customers to longer subscription intervals (for example, from monthly to yearly) can increase your average order value and cash flow.

All recurring prices that aren’t metered are eligible to use subscription upsells. For any eligible price, you can set up a subscription upsell to another price that meets the following criteria:

*   Prices must reference the same [Product](/api/prices/object#price_object-product).
*   Prices must have the same [currency](/api/prices/object#price_object-currency).
*   Prices must be `recurring` [type](/api/prices/object#price_object-type).
*   If your prices use [tax behavior](/api/prices/object#price_object-tax_behavior), their values must be identical.
*   If your price uses [tiers](/api/prices/object#price_object-tiers), the value for `up_to` in each tier must be identical.
*   If using [quantity transformation](/api/prices/object#price_object-transform_quantity), the values for `divide_by` and `round` must be identical.

Create a subscription upsell
----------------------------

Configure a subscription upsell in the Dashboard on the Price details page. To view the details for a Price, select a Product and select a price associated with the Product. In the Upsells section, select an upsell price from the dropdown menu. Upsells immediately apply to eligible Checkout Sessions that use that price.

![Configure a subscription upsell on the Price details page](https://b.stripecdn.com/docs-statics-srv/assets/add-upsell.08bc9bf9425295edb1ada9ff297ee257.gif)

Configure a subscription upsell on the Price details page.

Checkout flow
-------------

During checkout, customers see an option to select the upsell with savings displayed, if applicable. For a Checkout Session to be eligible for upsells, it must:

*   Be a subscription mode Checkout Session
*   Have only one `type=recurring` price in the Checkout Session
*   Have a valid configuration for the upsell price

Stripe calculates savings based on the amount the user saves in one billing cycle if they chose upsell pricing. For example, a monthly subscription of 100 USD that upsells to an annual subscription of 1000 USD shows savings of 200 USD. Checkout displays the savings as an amount or a percentage, depending on the character length of the savings.

Users can toggle between the initial price option and the upsell price option and then checkout.

![Toggle between the initial price option and the upsell price option](https://b.stripecdn.com/docs-statics-srv/assets/upsell-preview.2a43c1a8acb9f167178b7fda6a2b0796.gif)

Customer preview.

Retrieve Checkout Session line items
------------------------------------

After a customer selects an upsell, the `line_items` for the Checkout Session update to reflect the upsell price. When [fulfilling your order](/checkout/fulfillment#create-payment-event-handler) using the `checkout.session.completed` webhook, make sure to [retrieve the line items](/api/checkout/sessions/line_items).

Trial behavior
--------------

If a customer selects an upsell for a Checkout Session with a trial available, the trial length won’t change.

Coupon behavior
---------------

If you pass a coupon to the [discounts](/api/checkout/sessions/create#create_checkout_session-discounts) array of the Checkout Session, that coupon is also applied to the upsell price if a customer selects the upsell. For example, if a monthly subscription upsells to a yearly subscription, and you pass in a 50% off coupon with a duration of four months, the discount applies to all invoices in the four month period starting when the coupon is first applied. If the customer selects the upsell, the 50% discount applies to the entire yearly subscription because the yearly invoice is created during the coupon’s four month period.

Remove a subscription upsell
----------------------------

You can remove a subscription upsell on the Price details page. After you remove a subscription upsell, that upsell won’t be available to any new Checkout Sessions.

![Remove an upsell](https://b.stripecdn.com/docs-statics-srv/assets/remove-upsell.36e5e59619f3c13f0aa94a3bd48bafdb.gif)

Remove an upsell.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Create a subscription upsell](#create-upsell "Create a subscription upsell")

[Checkout flow](#checkout-flow "Checkout flow")

[Retrieve Checkout Session line items](#line-items "Retrieve Checkout Session line items")

[Trial behavior](#trial-behavior "Trial behavior")

[Coupon behavior](#coupon-behavior "Coupon behavior")

[Remove a subscription upsell](#remove-upsell "Remove a subscription upsell")

Products Used

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/billing-cycle

 Définir la date du cycle de facturation | Documentation Stripe     

[Accéder directement au contenu](#main-content)

Définir la date de début de cycle de facturation

[

Créez un compte



](https://dashboard.stripe.com/register)ou[

connecter-vous



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fbilling-cycle)

[

](/)

Rechercher dans la documentation

/

[Créez un compte](https://dashboard.stripe.com/register)

[

Connectez-vous



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fbilling-cycle)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Plateformes et places de marché



](/connect)

[

Services bancaires



](/financial-services)

[

Outils de développement



](/development)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Plateformes et places de marché



](/connect)

[

Services bancaires



](/financial-services)

API et SDK

Aide

[Aperçu](/payments)

À propos des paiements Stripe

[Mettre votre intégration à niveau](/payments/upgrades "Améliorer votre intégration existante")

Analyses des paiements

Paiements en ligne

[Présentation](/payments/online-payments "Découvrez les possibilités d'intégration pour accepter des paiements en ligne.")[Trouver votre cas d'usage](/payments/use-cases/get-started "Découvrez comment Stripe peut accompagner votre entreprise.")

Use Payment Links

Créer une page de paiement

[Présentation](/payments/checkout/build-integration "Créez une expérience de paiement avec Checkout.")

[Solutions de démarrage rapide](/payments/checkout/quickstarts "Démarrez avec des exemples de code.")

[Personnaliser l'apparence](/payments/checkout/customization "Contrôlez l'apparence de la page de paiement. Le degré de personnalisation dépend du produit que vous utilisez.")

[Collecter des informations supplémentaires](/payments/checkout/collect-additional-info "Collecter des informations comme des adresses et des numéros de téléphone lors du processus de paiement")

[Collecter des taxes](/payments/checkout/taxes)

[Mise à jour dynamique lors du paiement](/payments/checkout/dynamic-updates "Effectuez des mises à jour pendant que votre client procède au paiement.")

[Gérer votre catalogue de produits](/payments/checkout/product-catalog)

[Abonnements](/payments/subscriptions "Gérer des abonnements avec Checkout")

[Configurer des essais gratuits](/payments/checkout/free-trials)

[Définir une limite d'un abonnement par client](/payments/checkout/limit-subscriptions)

Définir la date de début de cycle de facturation

[Gérer les moyens de paiement](/payments/checkout/payment-methods)

[Offrir aux clients la possibilité de payer dans leur devise locale](/payments/checkout/adaptive-pricing)

[Ajouter des réductions, des ventes incitatives et des ventes croisées](/payments/checkout/promotions)

[Configurer des paiements futurs](/payments/checkout/save-and-reuse "Comment enregistrer les données de paiement de vos clients et les débiter ultérieurement")

[Enregistrer les coordonnées bancaires lors du paiement](/payments/checkout/save-during-payment "Enregistrer les coordonnées bancaires lors du paiement")

[Après le paiement](/payments/checkout/after-the-payment)

[Liste des modifications de Elements avec l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrer depuis l'ancienne version de Checkout](/payments/checkout/migration)

[Migrer vers Checkout pour utiliser Prices](/payments/checkout/migrating-prices)

Développer une intégration avancée

Développer une intégration dans l'application

Moyens de paiement

Ajouter des moyens de paiement

Gérer les moyens de paiement

Paiement accéléré avec Link

Interfaces de paiement

Payment Links

Checkout

Web Elements

Elements intégrés à l'application

Scénarios de paiement

Tunnels de paiement personnalisés

Acquisition flexible

Paiements par TPE

Terminal

Autres produits Stripe

Financial Connections

Cryptomonnaies

Climate

Payout Links

France

Français (France)

[Accueil](/ "Accueil")[Paiements](/payments "Paiements")Build a checkout page[Subscriptions](/payments/subscriptions "Subscriptions")

Définir la date du cycle de facturation
=======================================

Définissez le point d'ancrage du cycle de facturation d'un abonnement sur une date fixe.
----------------------------------------------------------------------------------------

Page hébergée par Stripe

Formulaire intégré

Composants intégrés

Version bêta publique

Lors de la création d’une session Checkout, vous pouvez définir explicitement le [début du cycle de facturation](/api/checkout/sessions/create#create_checkout_session-subscription_data-billing_cycle_anchor) d’un abonnement sur une date fixe (par exemple, le 1er du mois suivant). La date de début du cycle détermine la date de la première facture du montant total, c’est-à-dire la date à laquelle les clients sont facturés du montant total de l’abonnement. La date de début du cycle et la fréquence de [facturation](/products-prices/overview) déterminent également les dates de facturation à venir d’un abonnement. Par exemple, un abonnement mensuel créé le 15 mai avec une date de début du cycle de facturation fixée au 1er juin est facturé le 15 mai, puis tous les 1er de chaque mois.

Pour la période de facturation initiale jusqu’à la date de la première facture du montant total, vous pouvez personnaliser le traitement des [calculs au prorata](/billing/subscriptions/prorations) avec le paramètre [proration\_behavior](/api/checkout/sessions/create#create_checkout_session-subscription_data-proration_behavior). Par défaut, `proration_behavior` est défini sur `create_prorations`, et les clients reçoivent une [facture](/api/invoices "factures") calculée au prorata. Si `proration_behavior` est défini sur `none`, la période précédant la date de la première facture du montant total est gratuite.

Créer une session Checkout avec une date de début du cycle de facturation
-------------------------------------------------------------------------

Pour configurer un début de cycle de facturation, définissez le paramètre `subscription_data.billing_cycle_anchor` lorsque vous créez une session Checkout en mode `subscription`. La date de début du cycle de facturation doit être un horodatage UNIX postérieur à la date du jour et antérieur à la prochaine date de facturation de l’abonnement.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_VePHdqKTYQjKNInc7u56JBrQ  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=subscription \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})" \  -d "subscription_data[billing_cycle_anchor]"=1611008505`

Si la date de début du cycle de facturation se situe pendant la période active d’une session et qu’un client tente de payer une fois celle-ci passée, Checkout ne calcule pas de montant au prorata pour la période précédant la période de facturation, mais débite au contraire le client pour la totalité de la période (à compter de la date de début du cycle de facturation).

Désactiver les calculs au prorata
---------------------------------

Pour désactiver les calculs au prorata, définissez le paramètre `subscription_data.proration_behavior` sur `none` lorsque vous créez une session Checkout.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_VePHdqKTYQjKNInc7u56JBrQ  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=subscription \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})" \  -d "subscription_data[billing_cycle_anchor]"=1611008505 \  -d "subscription_data[proration_behavior]"=none`

Comme un essai gratuit, la période initiale jusqu’au début du cycle de facturation est gratuite. Contrairement à ce qui se passe avec un essai gratuit, aucune facture de 0 USD n’est générée. Les clients reçoivent une facture avec le montant total de l’abonnement à la date de début du cycle de facturation.

Dans l’objet Checkout Session response, les montants associés aux [postes de facture](/api/checkout/sessions/object#checkout_session_object-line_items) et aux [totaux](/api/checkout/sessions/object#checkout_session_object-total_details) sont toujours de 0 lorsque les calculs au prorata sont désactivés. Par ailleurs, l’[état du paiement](/api/checkout/sessions/object#checkout_session_object-payment_status) de la session est défini sur `no_payment_required`, ce qui indique que le paiement est reporté.

Limites actuelles
-----------------

*   Vous ne pouvez pas utiliser des périodes d’essai avec des dates de début du cycle de facturation dans Checkout.
*   Les tarifs ponctuels ne peuvent pas être utilisés dans des sessions Checkout lorsque `proration_behavior` est défini sur `none`.
*   Vous ne pouvez pas appliquer de [coupons `amount_off`](/api/coupons/create#create_coupon-amount_off) à des sessions Checkout avec `create_prorations` comme `proration_behavior` par défaut.

Voir aussi
----------

*   [Calculs au prorata](/billing/subscriptions/prorations)

Cette page vous a-t-elle été utile ?

OuiNon

Besoin d'aide ? [Contactez le service Support](https://support.stripe.com/).

Rejoignez notre [programme d'accès anticipé](https://insiders.stripe.dev/).

Consultez notre [journal des modifications des produits](https://stripe.com/blog/changelog).

Des questions ? [Contactez l'équipe commerciale](https://stripe.com/contact/sales).

Propulsé par [Markdoc](https://markdoc.dev)

Inscrivez-vous pour recevoir les mises à jour destinées aux développeurs :

S'inscrire

Vous pouvez vous désabonner à tout moment. Lisez notre [politique de confidentialité](https://stripe.com/privacy).

Sur cette page

[Créer une session Checkout avec une date de début du cycle de facturation](#create-session "Créer une session Checkout avec une date de début du cycle de facturation")

[Désactiver les calculs au prorata](#disable-prorations "Désactiver les calculs au prorata")

[Limites actuelles](#limitations "Limites actuelles")

[Voir aussi](#see-also "Voir aussi")

Produits utilisés

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

Le shell Stripe est plus optimisé sur la version bureau.

    $

---

## URL: https://docs.stripe.com/payments/checkout/phone-numbers

 Collect customer phone numbers | Documentazione Stripe     

[Passa al contenuto](#main-content)

Raccogliere i numeri di telefono

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fphone-numbers)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fphone-numbers)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Raccogliere gli indirizzi fisici](/payments/collect-addresses "Come raccogliere gli indirizzi di fatturazione e spedizione.")

[Addebitare la spedizione](/payments/during-payment/charge-shipping)

Raccogliere i numeri di telefono

[Aggiungi campi personalizzati](/payments/checkout/custom-fields)

[Ottenere il consenso per email promozionali](/payments/checkout/promotional-emails-consent)

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page[Collect additional information](/payments/checkout/collect-additional-info "Collect additional information")

Collect customer phone numbers
==============================

Collect a phone number for shipping or invoicing when your customer makes a payment.
------------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

You can enable phone number collection on all `payment` and `subscription` [mode](/api/checkout/sessions/create#create_checkout_session-mode) Sessions (phone number collection isn’t supported in `setup` mode). Only collect phone numbers if you need them for the transaction.

[

Enable phone number collection


--------------------------------





](#create-session)

To enable phone number collection, set [phone\_number\_collection\[enabled\]](/api/checkout/sessions/create#create_checkout_session-phone_number_collection-enabled) to `true` when creating a Checkout Session.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d "line_items[0][price_data][unit_amount]"=1000 \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][currency]"=eur \  -d "line_items[0][quantity]"=2 \  -d "phone_number_collection[enabled]"=true \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

With phone number collection enabled, Checkout adds a _required_ phone number field to the payment form. If you’re collecting a shipping address, the phone number field displays under the address fields. Otherwise, Checkout displays the phone number field below the email input. Customers can only enter one phone number per session.

[

Retrieve the phone number


---------------------------





](#after-session)

### Phone number format

When your customer checks out with third-party wallets such as [Apple Pay](/apple-pay), or [Google Pay](/google-pay), the phone number format isn’t guaranteed because of limitations on those platforms. Checkout attempts to save phone numbers from third-party wallets in [E.164](https://en.wikipedia.org/wiki/E.164) format when possible. In all other cases, when a customer doesn’t use [Apple Pay](/apple-pay), or [Google Pay](/google-pay), we guarantee phone numbers in [E.164](https://en.wikipedia.org/wiki/E.164) format.

After the session, you can retrieve customer phone numbers from the resulting [Customer](/api/customers "Clienti"), or [Checkout Session](/api/checkout/sessions "sessione di Checkout") objects:

*   [On the Customer](/api/customers): Checkout saves collected phone numbers onto the [phone](/api/customers/object#customer_object-phone) property of the Customer object, which you can access programmatically by either fetching the Customer object directly with the [API](/api/customers/retrieve), or by listening for the [customer.created](/api/events/types#event_types-customer.created) event in a [webhook](/webhooks "webhook"). You can also view the customer’s phone number in the [dashboard](https://dashboard.stripe.com/customers).
*   [On the Checkout Session](/api/checkout/sessions): The customer’s phone number is also saved in the [customer\_details](/api/checkout/sessions/object#checkout_session_object-customer_details) hash of the Checkout Session object, under [customer\_details.phone](/api/checkout/sessions/object#checkout_session_object-customer_details-phone). After each successful Checkout Session, Stripe emits the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event containing the Checkout Session object (and phone number), which you can listen for in a [webhook](/webhooks "webhook").

[

Collect phone numbers for existing customers


----------------------------------------------





](#existing-customers)

Passing in an existing [Customer](/api/customers) with a populated [phone](/api/customers/object#customer_object-phone) property to the [Checkout Session](/api/checkout/sessions) results in the phone number field being prefilled.

If the customer updates their phone number, this updated value persists on the [phone](/api/checkout/sessions/object#checkout_session_object-phone) property on the [Customer object](/api/customers) , overwriting any previously saved phone number.

### Update phone numbers with the customer portal

You can allow customers to manage their own accounts (which includes [updating their phone numbers](/api/customer_portal/configurations/create#create_portal_configuration-features-customer_update-allowed_updates)) in the customer portal.

Vedi anche
----------

*   [Integrate the customer portal](/customer-management)

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Enable phone number collection](#create-session "Enable phone number collection")

[Retrieve the phone number](#after-session "Retrieve the phone number")

[Collect phone numbers for existing customers](#existing-customers "Collect phone numbers for existing customers")

[Update phone numbers with the customer portal](#phone-number-updates "Update phone numbers with the customer portal")

[Vedi anche](#see-also "Vedi anche")

Prodotti utilizzati

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/taxes

 Collect taxes | Stripe Documentation     

[Skip to content](#main-content)

Collect taxes

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Ftaxes)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Ftaxes)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

Collect taxes

[Use manual tax rates](/payments/checkout/use-manual-tax-rates)

[Collect tax IDs](/tax/checkout/tax-ids)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

Collect taxes
=============

Learn how to collect taxes with Stripe Tax.
-------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Stripe Tax allows you to calculate the tax on your one-time and recurring payments when you use Checkout. You can enable Stripe Tax to automatically compute taxes on all of your Checkout purchases and subscriptions.

[

Activate Stripe Tax


---------------------





](#activate)

[Log in](https://dashboard.stripe.com/settings/tax) or [sign up](https://dashboard.stripe.com/register) for Stripe to activate Stripe Tax.

Update your Products and Prices
-------------------------------

When calculating tax, Stripe Tax uses information stored on the [Products](/api/products "Products") and [Prices](/api/prices "Prices") APIs to determine the right rates and rules. You can update your Checkout products and prices to include:

*   `tax_behavior`—Specifies whether the price is considered `inclusive` or `exclusive` of taxes.
*   `tax_code` (_optional_)—Specifies the product tax code. If you don’t set a `tax_code` on a product, we apply your preset product tax code. For more information, consult our [list of tax codes](/tax/tax-codes).

When you set the `tax_behavior` parameter to `exclusive`, it adds tax to the subtotal. This is common in US markets and for business-to-business (B2B) sales. If you set the `tax_behavior` to `inclusive`, the amount your buyer pays never changes (even if the tax rate varies). This is common practice for business-to-consumer (B2C) buyers in markets outside of the US. If you don’t want to create your products and prices upfront, you can pass the `price_data.tax_behavior` and `product_data.tax_code` parameters in your Checkout session.

#### Note

Learn more about [Products, prices, tax codes, and tax behavior](/tax/products-prices-tax-codes-tax-behavior).

Create a Checkout Session
-------------------------

After updating your products and prices, you’re ready to start calculating tax on your Checkout sessions. You can create sessions for one-time and recurring purchases.

To calculate tax for new customers, Checkout validates and uses the provided shipping or billing address. For existing customers, Checkout calculates tax by validating and using the attached customer shipping or billing address. If you capture a new billing or shipping address for an existing customer, Checkout won’t automatically override the previous billing or shipping information. You must explicitly request customer address changes.

### Apple Pay and Google Pay

If you wish to ensure that Google Pay is offered as a payment method while using Stripe Tax in Checkout, you must require collecting a shipping address. Apple Pay with Stripe Tax displays only when the customer’s browser supports Apple Pay version 12 or greater.

Calculate tax for new customers
-------------------------------

If you don’t pass in an existing customer when creating a Checkout session, Checkout creates a new customer and automatically saves the billing address and shipping information. Checkout uses the shipping address entered during the session to determine the customer’s location for calculating tax. If you don’t collect shipping information, Checkout uses the billing address.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=2 \  -d "automatic_tax[enabled]"=true \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

[

OptionalCalculate tax for existing customers


----------------------------------------------





](#existing-customers)

[

OptionalCheck the response


----------------------------





](#check-the-response)

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Activate Stripe Tax](#activate "Activate Stripe Tax")

[Update your Products and Prices](#product-and-price-setup "Update your Products and Prices")

[Create a Checkout Session](#create-session "Create a Checkout Session")

[Apple Pay and Google Pay](#apple-pay-and-google-pay "Apple Pay and Google Pay")

[Calculate tax for new customers](#new-customers "Calculate tax for new customers")

Products Used

[

Checkout





](/payments/checkout)

[

Tax





](/tax)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/analyze-conversion-funnel

 Analyze your conversion funnel | Stripe Documentation     

[Skip to content](#main-content)

Analyze conversion funnel

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fanalyze-conversion-funnel)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fanalyze-conversion-funnel)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Fulfill orders](/checkout/fulfillment)

[Send receipts and paid invoices](/payments/checkout/receipts)

[Customize redirect behavior](/payments/checkout/custom-success-page)

[Recover abandoned carts](/payments/checkout/abandoned-carts)

Analyze conversion funnel

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Spain

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[After the payment](/payments/checkout/after-the-payment "After the payment")

Analyze your conversion funnel
==============================

Analyze your Stripe Checkout conversion funnel with Google Analytics 4.
-----------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Use Google Analytics 4 (GA4) to track users as they progress through your Stripe Checkout purchase funnel. Before you begin, set up a [GA4 account](https://support.google.com/analytics/answer/9304153) and add a [GA4 property](https://support.google.com/analytics/answer/9744165?hl=en#zippy=%2Cin-this-article).

Set up your site
----------------

1.  Create a product page with a **Checkout** button:
    
    product.html
    
    `<html>   <head>     <title>Buy cool new product</title>   </head>   <body>     <script>       window.addEventListener("load", function () {         document           .getElementById("submit")           .addEventListener("click", function (event) {             event.preventDefault();             fetch("/create-checkout-session", {               method: "POST",             })               .then((response) => response.json())               .then((checkoutSession) => {                 window.location.href = checkoutSession.url;               });           });       });     </script>     <form>       <button id="submit">Checkout</button>     </form>   </body> </html>`
    
2.  Create a server-side endpoint that creates a Checkout Session and serves the pages:
    
    index.js
    
    ``// This example sets up endpoints using the Express framework. // Watch this video to get started: [https://youtu.be/rPR2aJ6XnAc.](https://youtu.be/rPR2aJ6XnAc)  const express = require("express"); require("dotenv").config();  const app = express();  // Set your secret key. Remember to switch to your live key in production! // See your keys here: [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)  const stripe = require('stripe')(  'sk_test_CGGvfNiIPwLXiDwaOfZ3oX6Y'  );  const request = require("request");  app.post(   "/create-checkout-session",   express.urlencoded({ extended: false }),   async (req, res) => {     const session = await stripe.checkout.sessions.  create  ({       payment_method_types: ["card"],       line_items: [         {           price_data: {             currency: "usd",             product_data: {               name: "T-shirt",             },             unit_amount: 2000,           },           quantity: 1,         },       ],       mode: "payment",       success_url: req.get("origin") + "/success",       cancel_url: req.get("origin") + "/cancel",     });      res.json({ url: session.url });   } );  app.get("/product", function (req, res) {   res.sendFile(__dirname + "/product.html"); });  app.get("/success", function (req, res) {   res.sendFile(__dirname + "/success.html"); });  app.get("/cancel", function (req, res) {   res.sendFile(__dirname + "/cancel.html"); });  app.listen(4242, () => console.log(`Listening on port ${4242}!`));``
    
3.  Create a success page:
    
    success.html
    
    `<html>   <head>     <title>Thanks for your order!</title>   </head>   <body>     <h1>Thanks for your order!</h1>     <p>       We appreciate your business! If you have any questions, please email       <a href="mailto:orders@example.com">orders@example.com</a>.     </p>   </body> </html>`
    
4.  Create a canceled page:
    
    canceled.html
    
    `<html>   <head>     <title>Order Canceled!</title>   </head>   <body>     <p>       <a href="/product">Start another order</a>.     </p>   </body> </html>`
    

Instrumentation walkthrough
---------------------------

In the following example, we assume your customer has:

*   Viewed your product page.
*   Clicked the **Buy** button and was redirected to Stripe Checkout.
*   Completed the payment and was redirected to the success page.

### Quick summary

### Add instrumentation

1.  Add `checkout.stripe.com` to your referral exclusion list.
    
2.  Add Google Analytics tags to your product, success, and canceled pages. Tags automatically fire an event on page load.
    
    product.html
    
    `<html>   <head>     <!-- START GOOGLE ANALYTICS -->     <script       async       src="[https://www.googletagmanager.com/gtag/js?id=](https://www.googletagmanager.com/gtag/js?id=)<GOOGLE_ANALYTICS_CLIENT_ID>"     ></script>     <script>       window.dataLayer = window.dataLayer || [];       function gtag() {         window.dataLayer.push(arguments);       }       gtag("js", new Date());       gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");     </script>     <!-- END GOOGLE ANALYTICS -->     <title>Buy cool new product</title>   </head>   <body>     <script>       window.addEventListener("load", function () {         document           .getElementById("submit")           .addEventListener("click", function (event) {             event.preventDefault();             fetch("/create-checkout-session", {               method: "POST",             })               .then((response) => response.json())               .then((checkoutSession) => {                 window.location.href = checkoutSession.url;               });           });       });     </script>     <form>       <button id="submit">Checkout</button>     </form>   </body> </html>`
    
    success.html
    
    `<html>   <head>     <!-- START GOOGLE ANALYTICS -->     <script       async       src="[https://www.googletagmanager.com/gtag/js?id=](https://www.googletagmanager.com/gtag/js?id=)<GOOGLE_ANALYTICS_CLIENT_ID>"     ></script>     <script>       window.dataLayer = window.dataLayer || [];       function gtag() {         window.dataLayer.push(arguments);       }       gtag("js", new Date());       gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");     </script>     <!-- END GOOGLE ANALYTICS -->     <title>Thanks for your order!</title>   </head>   <body>     <h1>Thanks for your order!</h1>     <p>       We appreciate your business! If you have any questions, please email       <a href="mailto:orders@example.com">orders@example.com</a>.     </p>   </body> </html>`
    
    canceled.html
    
    `<html>   <head>     <!-- START GOOGLE ANALYTICS -->     <script       async       src="[https://www.googletagmanager.com/gtag/js?id=](https://www.googletagmanager.com/gtag/js?id=)<GOOGLE_ANALYTICS_CLIENT_ID>"     ></script>     <script>       window.dataLayer = window.dataLayer || [];       function gtag() {         window.dataLayer.push(arguments);       }       gtag("js", new Date());       gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");     </script>     <!-- END GOOGLE ANALYTICS -->     <title>Order Canceled!</title>   </head>   <body>     <p>       <a href="/product">Start another order</a>.     </p>   </body> </html>`
    
3.  Fire an event just before redirecting to Stripe Checkout:
    
    product.html
    
    `<html>   <head>     <!-- START GOOGLE ANALYTICS -->     <script       async       src="[https://www.googletagmanager.com/gtag/js?id=](https://www.googletagmanager.com/gtag/js?id=)<GOOGLE_ANALYTICS_CLIENT_ID>"     ></script>     <script>       window.dataLayer = window.dataLayer || [];       function gtag() {         window.dataLayer.push(arguments);       }       gtag("js", new Date());       gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");     </script>     <!-- END GOOGLE ANALYTICS -->     <title>Buy cool new product</title>   </head>   <body>     <script>       window.addEventListener("load", function () {         document           .getElementById("submit")           .addEventListener("click", function (event) {             event.preventDefault();             fetch("/create-checkout-session", {               method: "POST",             })               .then((response) => response.json())               .then((checkoutSession) => {                 window.location.href = checkoutSession.url;                 gtag("event", "begin_checkout", {                   event_callback: function () {                     window.location.href = checkoutSession.url;                   },                 });               });           });       });     </script>     <form>       <button id="submit">Checkout</button>     </form>   </body> </html>`
    

### Analyze your conversion funnel metrics

After you add the proper instrumentation, you can see the metrics corresponding to each step defined in your conversion funnel:

*   **product page views:** The number of page visitors who viewed the product page.
*   **begin\_checkout event count:** The number of page visitors who clicked the **Buy** button and were redirected to Stripe Checkout.
*   **success page views:** The number of page visitors who completed the purchase and were redirected to the success page.

Using these numbers, you can see where visitors are dropping off in your conversion funnel.

[

OptionalServer-side event recording


-------------------------------------





](#server-side-event-recording)

[

OptionalLinking client and server-side events


-----------------------------------------------





](#link-client-and-server-side-events)

[

OptionalServer-side redirects


-------------------------------





](#server-side-redirect)

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Set up your site](#setup "Set up your site")

[Instrumentation walkthrough](#instrumentation-using-google-analytics "Instrumentation walkthrough")

[Add instrumentation](#adding-instrumentation "Add instrumentation")

[Analyze your conversion funnel metrics](#analysis "Analyze your conversion funnel metrics")

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/how-checkout-works

 How Checkout works | Stripe Documentation     

[Skip to content](#main-content)

How Checkout works

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

[Overview](/payments/checkout)

How Checkout works

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Checkout

How Checkout works
==================

Learn how to use Checkout to collect payments on your website.
--------------------------------------------------------------

Checkout is a low-code payment integration that creates a customizable form for collecting payments.

Checkout’s built-in features allow you to reduce your development time. It supports 40+ payment methods, including [Link](/payments/link), which lets your customers save their payment method for faster checkout. You can accept payments by embedding Checkout directly into your website, redirecting customers to a Stripe-hosted payment page, or creating a customized checkout page with [Stripe Elements](/payments/elements). Checkout supports payments for both [one-time purchases](/payments/online-payments) and [subscriptions](/subscriptions).

You can also customize Checkout and access additional functionality with the [Checkout Sessions API](/api/checkout/sessions) and the Stripe Dashboard. For a complete list of features, see its [built-in and customizable features](/payments/checkout/how-checkout-works#features).

Stripe-hosted page

Embedded form

Embedded components

Public preview

Checkout lifecycle
------------------

1.  When customers are ready to complete their purchase, your application creates a new Checkout Session.
2.  The Checkout Session provides a URL that redirects customers to a Stripe-hosted payment page.
3.  Customers enter their payment details on the payment page and complete the transaction.
4.  After the transaction, a [webhook](/webhooks "webhook") [fulfills the order](/checkout/fulfillment) using the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event.

Client

Server

Stripe API

Stripe Checkout

Send order information

Create Checkout Session

Return Checkout Session

checkout.session.created

Redirect customer to `url` from Checkout Session

Customer completes payment

Customer returns to your application

Handle fulfillment

checkout.session.completed

A diagram of a Stripe-hosted page integration's lifecycle

Low-code integration
--------------------

Checkout requires minimal coding and is the best choice for most integrations because of its prebuilt functionalities and customization options. You can integrate Checkout by creating a Checkout Session and collecting customer payment details. Collect payments by redirecting customers to a [Stripe-hosted payment page](/payments/accept-a-payment?platform=web&ui=stripe-hosted).

[Compare Checkout](/payments/online-payments#compare-features-and-availability) to other Stripe payment options to determine the best one for you. Checkout displays a payment form to collect customer payment information, validates cards, handles errors, and so on.

Built-in and customizable features
----------------------------------

Stripe Checkout has the following built-in and customizable features:

### Built-in features

*   Support for digital wallets and Link
*   Responsive mobile design
*   SCA-ready
*   CAPTCHAs
*   PCI compliance
*   Card validation
*   Error messaging
*   [Adjustable quantities](/payments/checkout/adjustable-quantity)
*   [Automatic tax collection](/tax/checkout)
*   International language support
*   [Adaptive Pricing](/payments/checkout/adaptive-pricing)

### Customizable features

*   [Collect taxes](/payments/checkout/taxes)
*   [Custom branding with colors, buttons, and font](/payments/checkout/customization)
*   [Cross-sells](/payments/checkout/cross-sells)
*   [Global payment methods](/payments/dashboard-payment-methods)
*   [Subscription upsells](/payments/checkout/upsells)
*   [Custom domains](/payments/checkout/custom-domains) (Stripe-hosted page only)
*   [Email receipts](/receipts)
*   [Apply discounts](/payments/checkout/discounts)
*   [Custom success page](/payments/checkout/custom-success-page)
*   [Recover abandoned carts](/payments/checkout/abandoned-carts)
*   [Autofill payment details with Link](/payments/checkout/customization/behavior#link)
*   [Collect Tax IDs](/tax/checkout/tax-ids)
*   [Collect shipping information](/payments/collect-addresses?payment-ui=checkout)
*   [Collect phone numbers](/payments/checkout/phone-numbers)
*   [Set the subscription billing cycle date](/payments/checkout/billing-cycle)

### Custom branding

You can set fonts, colors, icons, and field styles for your Stripe-hosted Checkout page using the [Branding settings](https://dashboard.stripe.com/settings/branding/checkout) in the Dashboard. For more information, see [Customize your integration](/payments/checkout/customization).

### Custom domains

If you use Stripe’s [custom domain feature](/payments/checkout/custom-domains), you can serve Stripe-hosted Checkout pages on a subdomain of your custom domain. Custom domains are a paid feature. For information, see [Pricing and fees](https://stripe.com/pricing).

Checkout Session
----------------

The Checkout Session is a programmatic representation of what your customers see on the checkout page. After creating a Checkout Session, redirect your customers to the Session’s URL to complete the purchase. When customers complete their purchase, you can [fulfill their orders](/checkout/fulfillment) by configuring an [event destination](/event-destinations) to process Checkout Session events. This code snippet from the [quickstart guide](/checkout/quickstart) is an example of how to create a Checkout Session in your application.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

### One-time and recurring payments

Allow customers to make one-time payments or subscribe to a product or service by setting the [mode](/api/checkout/sessions/create#create_checkout_session-mode) parameter in a Checkout Session.

Mode

Purchase type

Payment

One-time purchases

[Subscription](/billing/subscriptions/overview)

*   Recurring purchases
*   Mixed cart: Recurring purchases with one-time purchases

### Mixed cart

Create a mixed cart in Checkout that lets your customers purchase Subscription items and one-time purchase items at the same time. To create a mixed cart, set the `mode` parameter to `subscription` and include the Price IDs, or `price_data`, for each line\_item in the [line\_items](/api/checkout/sessions/create#create_checkout_session-line_items) array. Price IDs come from Price objects created using the Stripe Dashboard or API and allow you to store information about your product catalog in Stripe.

You can also use [price\_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data) to reference information from an external database where you’re hosting price and product details without storing product catalog information on Stripe. For more information, see [Build a subscriptions integration](/billing/subscriptions/build-subscriptions).

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"={{RECURRING_PRICE_ID}} \   -d "line_items[0][quantity]"=1 \  -d "line_items[1][price]"={{ONE_TIME_PRICE_ID}} \   -d "line_items[1][quantity]"=1 \  -d mode=subscription \   --data-urlencode success_url="https://example.com/success" \   --data-urlencode cancel_url="https://example.com/cancel"`

### Payment methods

You can view, enable, and disable different payment methods in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) at any time. Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. View our [complete list of payment methods](/payments/payment-methods/overview).

### Save payment details and default payment methods

You can [save payment details for future use](/payments/save-and-reuse) by sending an API parameter when you create a Session. Options to save payment details include:

*   **Single payment**: If your Checkout Session uses `payment` mode, set the [payment\_intent\_data.setup\_future\_usage](/payments/payment-intents#future-usage) parameter.
*   **Subscription payment**: If your Checkout Session uses `subscription` mode, Stripe saves the payment method by default.
*   [Multiple saved payment methods](/payments/accept-a-payment?platform=web&ui=checkout#save-payment-method-details): If a customer has multiple payment methods saved, you can store a default payment method to the Customer object’s [default\_payment\_method](/api/customers/object#customer_object-invoice_settings-default_payment_method) field. However, these payment methods don’t appear for return purchases in Checkout.

### Guest customers

The `Customer` object represents a customer of your business, and it helps tracking subscriptions and payments that belong to the same customer. Checkout Sessions that don’t create Customers are associated with [guest customers](/payments/checkout/guest-customers) instead.

Complete a transaction
----------------------

To automate business flows after a transaction has occurred, register an [event destination](/event-destinations) and build a [webhook endpoint handler](/webhooks/quickstart). Consider the following events and automations to enable:

*   Process the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event to fullfill orders when a customer completes their purchase.
*   Process the [checkout.session.expired](/api/events/types#event_types-checkout.session.expired) event to return items to your inventory or send users a cart [abandonment](/payments/checkout/abandoned-carts) email when they don’t make a purchase and their cart expires.

See also
--------

*   [Checkout quickstart](/checkout/quickstart)
*   [Fulfill your orders](/checkout/fulfillment)
*   [Collect taxes in Checkout](/payments/checkout/taxes)
*   [Manage limited inventory with Checkout](/payments/checkout/managing-limited-inventory)
*   [Automatically convert to local currencies with Adaptive Pricing](/payments/checkout/adaptive-pricing)

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Checkout lifecycle](#lifecycle "Checkout lifecycle")

[Low-code integration](#low-code "Low-code integration")

[Built-in and customizable features](#features "Built-in and customizable features")

[Built-in features](#built-in "Built-in features")

[Customizable features](#customizable "Customizable features")

[Custom branding](#branding "Custom branding")

[Custom domains](#custom-domains "Custom domains")

[Checkout Session](#session "Checkout Session")

[One-time and recurring payments](#checkout-mode "One-time and recurring payments")

[Mixed cart](#mixed-cart "Mixed cart")

[Payment methods](#payment-methods "Payment methods")

[Save payment details and default payment methods](#save-payment-methods "Save payment details and default payment methods")

[Guest customers](#guest-customers "Guest customers")

[Complete a transaction](#complete-transaction "Complete a transaction")

[See also](#see-also "See also")

Related Guides

[

No-code options to accept payments on Stripe



](/no-code)

[

Prebuilt checkout page



](/checkout/quickstart)

[

Learn about payment methods



](/payments/payment-methods/overview)

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/

 Stripe Checkout | Documentation Stripe     

[Accéder directement au contenu](#main-content)

Présentation

[

Créez un compte



](https://dashboard.stripe.com/register)ou[

connecter-vous



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout)

[

](/)

Rechercher dans la documentation

/

[Créez un compte](https://dashboard.stripe.com/register)

[

Connectez-vous



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Plateformes et places de marché



](/connect)

[

Services bancaires



](/financial-services)

[

Outils de développement



](/development)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Plateformes et places de marché



](/connect)

[

Services bancaires



](/financial-services)

API et SDK

Aide

[Aperçu](/payments)

À propos des paiements Stripe

[Mettre votre intégration à niveau](/payments/upgrades "Améliorer votre intégration existante")

Analyses des paiements

Paiements en ligne

[Présentation](/payments/online-payments "Découvrez les possibilités d'intégration pour accepter des paiements en ligne.")[Trouver votre cas d'usage](/payments/use-cases/get-started "Découvrez comment Stripe peut accompagner votre entreprise.")

Use Payment Links

Créer une page de paiement

Développer une intégration avancée

Développer une intégration dans l'application

Moyens de paiement

Ajouter des moyens de paiement

Gérer les moyens de paiement

Paiement accéléré avec Link

Interfaces de paiement

Payment Links

Checkout

Présentation

[Fonctionnement de Checkout](/payments/checkout/how-checkout-works)

Web Elements

Elements intégrés à l'application

Scénarios de paiement

Tunnels de paiement personnalisés

Acquisition flexible

Paiements par TPE

Terminal

Autres produits Stripe

Financial Connections

Cryptomonnaies

Climate

Payout Links

France

Français (France)

[Accueil](/ "Accueil")[Paiements](/payments "Paiements")Checkout

Stripe Checkout
===============

Créez un formulaire de paiement nécessitant peu d'écriture de code et intégrez-le à votre site ou hébergez-le sur Stripe.
-------------------------------------------------------------------------------------------------------------------------

[Checkout](https://stripe.com/payments/checkout) est une intégration de paiement low-code qui permet de créer un formulaire personnalisable afin d’encaisser des paiements. Vous pouvez intégrer directement Checkout à votre site Web, rediriger les clients vers une page de paiement hébergée par Stripe ou créer une page de paiement personnalisée avec [Stripe Elements](https://stripe.com/payments/elements). Cette solution prend en charge les paiements ponctuels et les abonnements, et accepte plus de 40 moyens de paiement locaux. Pour obtenir la liste complète des fonctionnalités offertes par Checkout, consultez la section [Fonctionnalités intégrées et personnalisables](/payments/checkout#features).

[En savoir plus sur Stripe Checkout](https://checkout.stripe.dev)

![Formulaire de paiement hébergé](https://b.stripecdn.com/docs-statics-srv/assets/checkout-hosted-hover.180c6ab2498a8c65daefb5bedae835bf.png)

[Page hébergée par Stripe](/checkout/quickstart) : le client est redirigé vers une page de paiement hébergée par Stripe lorsqu’il est prêt à effectuer l’achat. Une fois qu’il a saisi ses coordonnées bancaires sur la page de paiement et effectué la transaction, il peut être redirigé vers votre site.

![Formulaire de paiement à l’aide d’Elements avec l’API Checkout Sessions](https://b.stripecdn.com/docs-statics-srv/assets/checkout-embedded-hover.14466c835d9723cfe90b3549956c451a.png)

[Formulaire intégré](/checkout/embedded/quickstart) : le client reste sur votre site et voit s’afficher une page de paiement personnalisée lorsqu’il est prêt à effectuer l’achat. Il saisit ses informations de paiement et effectue la transaction sur la même page de votre site, sans aucune redirection requise.

![Formulaire de paiement à l’aide d’Elements avec l’API Checkout Sessions](https://b.stripecdn.com/docs-statics-srv/assets/checkout-elements-hover.bfd33fb56dc4ec8915e4ab4601799f49.png)

[Embedded components](/checkout/custom/quickstart): Customizable checkout page built with Stripe Elements. Customers stay on your site and are shown a customized checkout page when they’re ready to complete their purchase. The customer enters their payment details and completes the transaction on the same page in your site so they don’t need to be redirected back to your site.

Démarrer
--------

[

Fonctionnement de Checkout

Découvrez comment ajouter une page Checkout à votre site Web et encaisser des paiements

](/payments/checkout/how-checkout-works "Fonctionnement de Checkout")

[

Regarder un tutoriel vidéo

Découvrez comment implémenter les fonctionnalités de Stripe Checkout pour les entreprises d’e-commerce et proposant des abonnements.

](https://www.youtube.com/watch?v=TJCdUYQTLJU "Regarder un tutoriel vidéo")

[

QuickStart

Découvrez un exemple de code d’intégration avec Stripe Checkout.

](/checkout/quickstart "QuickStart")

[

Activer des moyens de paiement internationaux

Activez différents moyens de paiement Checkout via le Dashboard.

](/payments/dashboard-payment-methods "Activer des moyens de paiement internationaux")

[

Traiter vos commandes

Découvrez comment traiter les commandes réglées par vos clients.

](/checkout/fulfillment "Traiter vos commandes")

Personnaliser Checkout
----------------------

[

Personnaliser votre intégration

Personnalisez votre image de marque, la prise en charge des langues, les polices, les politiques internes, etc.

](/payments/checkout/customization "Personnaliser votre intégration")

[

Utiliser des domaines personnalisés

Découvrez comment connecter votre domaine personnalisé à Stripe Checkout.

](/payments/checkout/custom-domains "Utiliser des domaines personnalisés")

[

Personnaliser votre page de confirmation de paiement

Affichez une page de confirmation personnalisée contenant les informations relatives à la commande de votre client.

](/payments/checkout/custom-success-page "Personnaliser votre page de confirmation de paiement")

[

Collecter des taxes

Collectez les taxes pour des paiements ponctuels.

](/payments/checkout/taxes "Collecter des taxes")

[

Collecter des numéros fiscaux

Collectez les numéros de TVA et autres numéros fiscaux des clients avec Checkout.

](/tax/checkout/tax-ids "Collecter des numéros fiscaux")

[

Collecter des numéros de téléphone

Collectez les numéros de téléphone dans Checkout.

](/payments/checkout/phone-numbers "Collecter des numéros de téléphone")

[

Factures post-paiement

Envoyez des factures à vos clients avec Stripe Checkout.

](/receipts?payment-ui=checkout "Factures post-paiement")

[

Configurer des paiements futurs

Enregistrez les données de paiement de vos clients et facturez-les ultérieurement.

](/payments/save-and-reuse "Configurer des paiements futurs")

Booster vos revenus
-------------------

[

Mises à niveau d'abonnements

Proposez à vos clients de passer à un abonnement supérieur au moment du paiement.

](/payments/checkout/upsells "Mises à niveau d'abonnements")

[

Ventes croisées

Offrez à vos clients la possibilité d’acheter des produits complémentaires lors du paiement grâce aux ventes croisées.

](/payments/checkout/cross-sells "Ventes croisées")

[

Récupération des paniers abandonnés

Récupérez des pages Checkout abandonnées et augmentez vos revenus.

](/payments/checkout/abandoned-carts "Récupération des paniers abandonnés")

[

Conversion automatique des devises grâce à Adaptive Pricing

Convertissez automatiquement vos tarifs dans la devise locale de vos clients pour augmenter votre taux de conversion.

](/payments/checkout/adaptive-pricing "Conversion automatique des devises grâce à Adaptive Pricing")

[

Définir des tarifs manuels pour chaque devise

Affichez les prix dans la devise locale de vos clients lors du paiement.

](/payments/checkout/manual-currency-prices "Définir des tarifs manuels pour chaque devise")

[

Analyser votre tunnel de conversion

Découvrez comment analyser le tunnel de conversion de votre page Stripe Checkout.

](/payments/checkout/analyze-conversion-funnel "Analyser votre tunnel de conversion")

Options sans code
-----------------

[

Grille tarifaire

Affichez une grille tarifaire sur votre site Web et redirigez directement vos clients vers Stripe Checkout.

](/payments/checkout/pricing-table "Grille tarifaire")

[

Liens de paiement

Intégrez ou partagez un lien vers une page de paiement Stripe pour accepter des paiements sans site Web.

](/payment-links "Liens de paiement")

Autres fonctionnalités
----------------------

[

Ajouter des réductions

Réduisez le montant facturé à un client en déduisant des bons de réduction ou des codes promotionnels du sous-total.

](/payments/checkout/discounts "Ajouter des réductions")

[

Facturer la livraison

Définissez des tarifs de livraison et recueillez les adresses de livraison de vos clients.

](/payments/during-payment/charge-shipping "Facturer la livraison")

[

Gérer un inventaire limité avec Checkout

Découvrez comment gérer vos stocks avec des périodes d’achat limitées dans le temps.

](/payments/checkout/managing-limited-inventory "Gérer un inventaire limité avec Checkout")

Essayer un exemple de projet
----------------------------

[

Paiements ponctuels

Web · Mobile web







](https://github.com/stripe-samples/checkout-one-time-payments "Paiements ponctuels")

[

Abonnements

Web · Mobile web · Stripe Billing







](https://github.com/stripe-samples/checkout-single-subscription "Abonnements")

[

Consulter nos exemples



](/samples)

Fonctionnalités intégrées et personnalisables
---------------------------------------------

Stripe Checkout propose les fonctionnalités suivantes :

### Fonctionnalités intégrées

*   Prise en charge des portefeuilles électroniques et de Link
*   Design mobile adaptatif
*   Mise en conformité avec la SCA
*   Utilisation de CAPTCHA
*   Conformité PCI
*   Validation de carte
*   Messages d’erreur
*   [Quantités ajustables](/payments/checkout/adjustable-quantity)
*   [Collecte automatique des taxes](/tax/checkout)
*   Prise en charge de nombreuses langues
*   [Adaptive Pricing](/payments/checkout/adaptive-pricing)

### Fonctionnalités personnalisables

*   [Collecte des taxes](/payments/checkout/taxes)
*   [Adaptation à votre marque au niveau des couleurs, boutons et polices](/payments/checkout/customization)
*   [Ventes croisées](/payments/checkout/cross-sells)
*   [Moyens de paiement internationaux](/payments/dashboard-payment-methods)
*   [Mises à niveau d’abonnements](/payments/checkout/upsells)
*   [Domaines personnalisés](/payments/checkout/custom-domains) (page hébergée par Stripe uniquement)
*   [Reçus par e-mail](/receipts)
*   [Application de réductions](/payments/checkout/discounts)
*   [Page de confirmation de paiement personnalisée](/payments/checkout/custom-success-page)
*   [Récupération des paniers abandonnés](/payments/checkout/abandoned-carts)
*   [Remplissage automatique des informations de paiement avec Link](/payments/checkout/customization/behavior#link)
*   [Collecter des numéros fiscaux](/tax/checkout/tax-ids)
*   [Collecte des informations de livraison](/payments/collect-addresses?payment-ui=checkout)
*   [Collecter les numéros de téléphone](/payments/checkout/phone-numbers)
*   [Définition de la date de début de facturation de l’abonnement](/payments/checkout/billing-cycle)

Inscrivez-vous pour recevoir un e-mail en cas de nouvelle fonctionnalité ou mise à jour.
----------------------------------------------------------------------------------------

Indiquez votre e-mail pour recevoir des actualités sur les nouvelles fonctionnalités et la prise en charge d'un plus grand nombre de cas d'usage.

Collect Email

Recevoir les mises à jour

Consultez notre [politique de confidentialité](https://stripe.com/privacy).

Cette page vous a-t-elle été utile ?

OuiNon

Besoin d'aide ? [Contactez le service Support](https://support.stripe.com/).

Rejoignez notre [programme d'accès anticipé](https://insiders.stripe.dev/).

Consultez notre [journal des modifications des produits](https://stripe.com/blog/changelog).

Des questions ? [Contactez l'équipe commerciale](https://stripe.com/contact/sales).

Propulsé par [Markdoc](https://markdoc.dev)

Inscrivez-vous pour recevoir les mises à jour destinées aux développeurs :

S'inscrire

Vous pouvez vous désabonner à tout moment. Lisez notre [politique de confidentialité](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

Le shell Stripe est plus optimisé sur la version bureau.

    $

---

## URL: https://docs.stripe.com/payments/checkout/custom-domains

 Use your custom domain | Documentazione Stripe     

[Passa al contenuto](#main-content)

Dominio personalizzato

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-domains)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-domains)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/get-started)[Explore all products](/products "Vedere tutti i prodotti disponibili di Stripe")[Fasi di rilascio](/release-phases "Come Stripe descrive le fasi di rilascio dei prodotti")

Pianificare l'integrazione

Configura Stripe

Crea un account

[Panoramica](/get-started/account "Attivare e gestire l'account Stripe")

[Attiva il tuo account](/get-started/account/activate "Attivare e proteggere l'account Stripe")

[Aggiungi fondi al tuo saldo](/get-started/account/add-funds "Aggiungi fondi al tuo saldo Stripe")

[Lista di controllo dell'account](/get-started/account/checklist "Completare questa lista di controllo prima di attivare l'account Stripe")

[Documenti di verifica accettabili](/acceptable-verification-documents)

Struttura dell'account

[Crea un team](/get-started/account/teams "Controlla gli accessi al tuo account Stripe")

[Organizations](/get-started/account/orgs "Gestire più account appartenenti a un'organizzazione")

[Account separati multipli](/get-started/account/multiple-accounts "Come creare e gestire più account Stripe")

[Conti esterni collegati](/get-started/account/linked-external-accounts "Gestire i conti esterni collegati a Stripe")

Impostazioni

[Branding](/get-started/account/branding "Personalizzare l'aspetto di email, procedura di pagamento, link di pagamento, portale cliente e fatture")

[Voci dell'estratto conto](/get-started/account/statement-descriptors "Come funzionano le voci per gli estratti conto")

[Dominio email personalizzato](/get-started/account/email-domain "Configurare il dominio utilizzato per l'invio delle email ai clienti")

Dominio personalizzato

[Single Sign-On](/get-started/account/sso "Single Sign-On")

[Accettare un pagamento](/payments/accept-a-payment)

Prodotti e prezzi

Utilizza Stripe senza dover scrivere codice

Assistenza per i regolamenti

Dashboard Stripe

Dashboard per il web

[Dashboard per dispositivi mobili](/dashboard/mobile)

Per sviluppatori

Avviare lo sviluppo

Progetti di esempio

Informazioni sulle API

Passare a Stripe

[Eseguire la migrazione dei dati dei clienti](/get-started/data-migrations "Eseguire la migrazione di dati di pagamento sensibili")

Eseguire la migrazione dei dati dei pagamenti

[Esegui la migrazione degli abbonamenti](/get-started/subscription-migrations "Eseguire la migrazione degli abbonamenti esistenti a Stripe")

Gestire il rischio di frode

Informazioni sulle frodi

Protezione contro le frodi di Radar

Gestisci le contestazioni

Verificare l'identità

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Inizia](/get-started "Inizia")Create an account

Use your custom domain
======================

Learn how to bring your own custom domain to Stripe Checkout, Payment Links, and customer portal.
-------------------------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

If you’re using the [Stripe-hosted page](/payments/accept-a-payment?platform=web&ui=stripe-hosted) for Checkout, you can add your own custom domain to Stripe. Adding custom domains is a paid feature. For information about cost, see Checkout’s [Pricing](https://stripe.com/pricing).

[

Add your custom domain to the Stripe Dashboard


------------------------------------------------





](#add-your-custom-domain)

Decide what subdomain to use with your Checkout Sessions, Payment Links, and customer portal.

#### Nota

If your domain is `example.com`, we recommend using `payments.example.com` as your custom subdomain. You can replace `payments` with anything you like, as long it’s a valid subdomain. You can’t use a path like `example.com/checkout` and must specify a subdomain of your existing domain.

After you decide on a subdomain, visit the [Custom domains settings page](https://dashboard.stripe.com/settings/custom-domains) to start the domain connection process.

On the settings page click **Add your domain**.

In the pop up, enter your desired subdomain. Click **Add** when you’re done. You’ll see the popup update with instructions for setting up your DNS records.

Your custom domain is activated automatically when your DNS records are verified. To disable this behavior, uncheck the **Switch to this domain once added** checkbox.

#### When will my domain be added?

When your domain is in the `Adding...` state, we wait to verify your DNS records that you set up in the next step. After Stripe verifies the DNS records, we create TLS certificates for your subdomain, set up the correct CDN routing, and then your domain is `ready` to enable and use.

[

Identify your DNS Provider


----------------------------





](#your-dns-provider)

To start, figure out what service is managing your DNS records, so you know exactly where to login and create the new records.

If you **already know** your DNS provider, you can move on to the next section.

Often, it’s the same place you registered your domain, but sometimes the DNS provider is different from your domain registrar.

If you’re not certain who your DNS provider is, try looking up your domain’s nameservers, replacing **stripe.com** with your own domain in this command:

Command Line

`nslookup -querytype=NS stripe.com`

You’ll see a list of nameservers for your domain in the output. Here’s some example output for **stripe.com**:

nslookup output

`# Looks like AWS is providing our DNS here: stripe.com	nameserver = ns-423.awsdns-52.com. stripe.com	nameserver = ns-705.awsdns-24.net. stripe.com	nameserver = ns-1087.awsdns-07.org. stripe.com	nameserver = ns-1882.awsdns-43.co.uk.`

If you’re more comfortable using a browser-based tool, go to [MXLookup’s DNS Lookup tool](https://mxtoolbox.com/DnsLookup.aspx) and enter your domain. It might be able to tell you who your DNS provider is (but not always).

[

Create required DNS records


-----------------------------





](#create-dns-records)

In this section, you’ll create the DNS records you need to connect your domain. As you go through each step, check each checkbox to keep track of where you are in the process.

Select the tab that matches your DNS provider from the tabs below—this gives you specific, guided instructions for creating the required DNS records. If your DNS provider isn’t an option, follow the Standard instructions:

Standard instructions

GoDaddy

Cloudflare

These are standard instructions for creating your DNS records. If you have issues with any of the steps, please contact your DNS provider for more assistance.

#### Nota

To track your progress, go through each step and check it off when you’ve completed it.

*   Sign into your DNS provider
    
    Most DNS providers have a control panel you can sign into to manage your DNS. Find your provider’s control panel page and sign in.
    
*   Find the page to manage the DNS for your domain
    
    Now that you’re logged in, find where you can manage the DNS records for your domain in your provider’s control panel.
    
    If you’re having issues finding the right page, you can:
    
    *   See if your DNS provider has a help article for adding new DNS records that can point you in the right direction.
    *   Contact your DNS provider for additional support.
*   Create your CNAME record
    
    From your DNS control panel, add a new record that maps your desired subdomain to Checkout. Most DNS providers ask you for the record type, name, value, and TTL or expiration when creating a new record.
    
    #### Nota
    
    This record is what connects your subdomain to Stripe Checkout.
    
    Enter these values and save the new DNS record:
    
    Field
    
    Instructions
    
    Description
    
    **Type**
    
    Select `CNAME` from the dropdown
    
    What kind of DNS record this is.
    
    **Name**
    
    If your custom subdomain is **checkout.powdur.me**, enter `checkout`
    
    For CNAME records, this field is the first part of your subdomain (the part leading up to the first period).
    
    **Value**
    
    Enter `hosted-checkout.stripecdn.com`
    
    This is what the new subdomain record points to–in this case, Stripe.
    
    Some providers may expect a trailing period (`.`) after the CNAME value. Make sure to verify that your CNAME value matches the format your provider expects.
    
    **TTL/Expiry**
    
    Enter `300`
    
    An expiration of 5 minutes (300 seconds) is OK. Your DNS provider might not allow you to change the TTL value. If this field is missing or you can’t change it, it’s safe to ignore this part of the configuration.
    
*   Create your TXT record
    
    From your DNS control panel, add a new TXT record.
    
    #### Nota
    
    This TXT record lets us verify that you’re the owner of this domain. This is required to issue TLS certificates for your domain, so you can continue to accept payments securely.
    
    Enter these values and save the new DNS record:
    
    Field
    
    Instructions
    
    Description
    
    **Type**
    
    Select `TXT` from the dropdown
    
    What kind of DNS record this is.
    
    **Name**
    
    If your custom domain is **checkout.powdur.me**, enter `_acme-challenge.checkout`
    
    For TXT records, this field is the subdomain portion of your domain.
    
    **Value**
    
    Visit the [Dashboard settings](https://dashboard.stripe.com/settings/custom-domains) and click **View instructions** to copy the correct TXT value record.
    
    This is a long, unique string used for domain verification.
    
    **TTL/Expiry**
    
    Enter `300`
    
    An expiration of 5 minutes (300 seconds) is OK. Your DNS provider might not allow you to change the TTL value. If this field is missing or you can’t change it, it’s safe to ignore this part of the configuration.
    
*   Verify your CNAME record is setup
    
    After you save your DNS record, verify that it has the correct values.
    
    Verify in your terminal
    
    Verify with your web browser
    
    1.  Wait up to 10 minutes for your DNS provider to update its nameservers.
    2.  Replace **checkout.powdur.me** with your custom domain in the following command and run it from your terminal:
    
    Command Line
    
    `nslookup -querytype=CNAME checkout.powdur.me`
    
    You should see output like:
    
    nslookup output
    
    `<your subdomain> 	canonical name = hosted-checkout.stripecdn.com.`
    
    When you see that output, move onto the next step.
    
*   Verify your TXT record
    
    After you save your DNS record, verify that it has the correct values.
    
    Verify in your terminal
    
    Verify with your web browser
    
    1.  Wait up to 10 minutes for your DNS provider to update its nameservers.
    2.  Replace **checkout.powdur.me** with your custom domain in the following command and run it from your terminal:
    
    Command Line
    
    `nslookup -querytype=TXT _acme-challenge.checkout.powdur.me`
    
    You should see output like this:
    
    nslookup output
    
    `_acme-challenge.<your domain>   text = "<your unique TXT record value>"`
    
    If you don’t see your unique TXT record value in the output, wait a bit longer and try running the command again.
    
    When you finish this step, your DNS records are configured.
    

Now that you’ve created your DNS records and verified them, Stripe verifies the connection and provisions your domain on our end. We’ll send you an email and a Dashboard notification when the domain is ready for you to enable it. You can also visit the [Dashboard settings](https://dashboard.stripe.com/settings/custom-domains) at any time to see the current status of your custom domain connection.

[

FacoltativoTest your custom domain


------------------------------------





](#test-your-domain)

[

FacoltativoRemoving your custom domain


----------------------------------------





](#removing-your-domain)

[

FacoltativoUsing custom domains with Connect


----------------------------------------------





](#connect)

[

FacoltativoTroubleshooting your integration


---------------------------------------------





](#troubleshooting-integration)

[

FacoltativoTroubleshooting CAA DNS records


--------------------------------------------





](#troubleshooting-caa-records)

[

FacoltativoTroubleshooting a blocked domain


---------------------------------------------





](#troubleshooting-a-blocked-domain)

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Add your custom domain to the Stripe Dashboard](#add-your-custom-domain "Add your custom domain to the Stripe Dashboard")

[Identify your DNS Provider](#your-dns-provider "Identify your DNS Provider")

[Create required DNS records](#create-dns-records "Create required DNS records")

Prodotti utilizzati

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/dynamic-updates

 Mettre à jour dynamiquement le paiement | Documentation Stripe     

[Accéder directement au contenu](#main-content)

Mise à jour dynamique lors du paiement

[

Créez un compte



](https://dashboard.stripe.com/register)ou[

connecter-vous



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fdynamic-updates)

[

](/)

Rechercher dans la documentation

/

[Créez un compte](https://dashboard.stripe.com/register)

[

Connectez-vous



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fdynamic-updates)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Plateformes et places de marché



](/connect)

[

Services bancaires



](/financial-services)

[

Outils de développement



](/development)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Plateformes et places de marché



](/connect)

[

Services bancaires



](/financial-services)

API et SDK

Aide

[Aperçu](/payments)

À propos des paiements Stripe

[Mettre votre intégration à niveau](/payments/upgrades "Améliorer votre intégration existante")

Analyses des paiements

Paiements en ligne

[Présentation](/payments/online-payments "Découvrez les possibilités d'intégration pour accepter des paiements en ligne.")[Trouver votre cas d'usage](/payments/use-cases/get-started "Découvrez comment Stripe peut accompagner votre entreprise.")

Use Payment Links

Créer une page de paiement

[Présentation](/payments/checkout/build-integration "Créez une expérience de paiement avec Checkout.")

[Solutions de démarrage rapide](/payments/checkout/quickstarts "Démarrez avec des exemples de code.")

[Personnaliser l'apparence](/payments/checkout/customization "Contrôlez l'apparence de la page de paiement. Le degré de personnalisation dépend du produit que vous utilisez.")

[Collecter des informations supplémentaires](/payments/checkout/collect-additional-info "Collecter des informations comme des adresses et des numéros de téléphone lors du processus de paiement")

[Collecter des taxes](/payments/checkout/taxes)

Mise à jour dynamique lors du paiement

[Personnalisation dynamique des options d'expédition](/payments/checkout/custom-shipping-options)

[Mise à jour dynamique des postes de facture](/payments/checkout/dynamically-update-line-items)

[Gérer votre catalogue de produits](/payments/checkout/product-catalog)

[Abonnements](/payments/subscriptions "Gérer des abonnements avec Checkout")

[Gérer les moyens de paiement](/payments/checkout/payment-methods)

[Offrir aux clients la possibilité de payer dans leur devise locale](/payments/checkout/adaptive-pricing)

[Ajouter des réductions, des ventes incitatives et des ventes croisées](/payments/checkout/promotions)

[Configurer des paiements futurs](/payments/checkout/save-and-reuse "Comment enregistrer les données de paiement de vos clients et les débiter ultérieurement")

[Enregistrer les coordonnées bancaires lors du paiement](/payments/checkout/save-during-payment "Enregistrer les coordonnées bancaires lors du paiement")

[Après le paiement](/payments/checkout/after-the-payment)

[Liste des modifications de Elements avec l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrer depuis l'ancienne version de Checkout](/payments/checkout/migration)

[Migrer vers Checkout pour utiliser Prices](/payments/checkout/migrating-prices)

Développer une intégration avancée

Développer une intégration dans l'application

Moyens de paiement

Ajouter des moyens de paiement

Gérer les moyens de paiement

Paiement accéléré avec Link

Interfaces de paiement

Payment Links

Checkout

Web Elements

Elements intégrés à l'application

Scénarios de paiement

Tunnels de paiement personnalisés

Acquisition flexible

Paiements par TPE

Terminal

Autres produits Stripe

Financial Connections

Cryptomonnaies

Climate

Payout Links

France

Français (France)

[Accueil](/ "Accueil")[Paiements](/payments "Paiements")Build a checkout page

Mettre à jour dynamiquement le paiement
=======================================

Effectuez des mises à jour pendant que votre client procède au paiement.
------------------------------------------------------------------------

[

Personnaliser dynamiquement les options d'expédition

Personnalisez les options d’expédition en fonction de l’adresse de livraison du client.

](/payments/checkout/custom-shipping-options "Personnaliser dynamiquement les options d'expédition")

[

Mettre à jour dynamiquement les postes

Mettez à jour des postes en fonction des modifications apportées lors du paiement

](/payments/checkout/dynamically-update-line-items "Mettre à jour dynamiquement les postes")

Cette page vous a-t-elle été utile ?

OuiNon

Besoin d'aide ? [Contactez le service Support](https://support.stripe.com/).

Rejoignez notre [programme d'accès anticipé](https://insiders.stripe.dev/).

Consultez notre [journal des modifications des produits](https://stripe.com/blog/changelog).

Des questions ? [Contactez l'équipe commerciale](https://stripe.com/contact/sales).

Propulsé par [Markdoc](https://markdoc.dev)

Inscrivez-vous pour recevoir les mises à jour destinées aux développeurs :

S'inscrire

Vous pouvez vous désabonner à tout moment. Lisez notre [politique de confidentialité](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

Le shell Stripe est plus optimisé sur la version bureau.

    $

---

## URL: https://docs.stripe.com/payments/checkout/payment-methods

 Manage payment methods | Stripe Documentation     

[Skip to content](#main-content)

Manage payment methods

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpayment-methods)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpayment-methods)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customise look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customisation depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information such as shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out")

[Manage your product catalogue](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

Manage payment methods

[Add one-click buttons](/checkout/one-click-payment-buttons)

[Migrate payment methods to the Dashboard](/payments/dashboard-payment-methods "Migrate to dynamic payment methods")

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment Methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Australia

English (United Kingdom)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

Manage payment methods
======================

Accepting more payment methods helps your business expand its global reach and improve checkout conversion.
-----------------------------------------------------------------------------------------------------------

Stripe dynamically displays the most relevant payment methods to your customers based on the payment method preferences you set in the Dashboard and eligibility factors such as transaction amount, currency, and payment flow. To enable and manage your payment method preferences, go to the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe enables certain payment methods for you by default and might enable additional payment methods after notifying you.

Manually specify payment methods
--------------------------------

You can override Dashboard settings by manually specifying [payment\_method\_types](/api/checkout/sessions/create#create_checkout_session-payment_method_types) when creating the Checkout Session. Unless your integration requires that you list payment methods manually, we recommend that you manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

If multiple payment methods are passed, Stripe dynamically reorders them to prioritize the most relevant payment methods based on the customer’s location and other characteristics.

[

Learn about payment methods

Explore the available options for global payment methods.

](/payments/payment-methods/overview "Learn about payment methods")

[

Add one-click payment buttons

Use one-click payment options, such as Apple Pay or Google Pay.

](/checkout/one-click-payment-buttons "Add one-click payment buttons")

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access programme](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/quickstarts

 Quickstarts | Stripe Documentation     

[Skip to content](#main-content)

Quickstarts

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fquickstarts)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fquickstarts)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

Quickstarts

[Create a Stripe-hosted checkout page](/checkout/quickstart "Hosted Checkout")

[Embed a payment form on your site](/checkout/embedded/quickstart "Embedded Checkout")

[Build a checkout page with embedded components](/checkout/custom/quickstart "Payments embedded components")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United Kingdom

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

Quickstarts
===========

Start quickly from sample projects.
-----------------------------------

Build a sample integration with Stripe Checkout.

See how this integration path [compares to Stripe’s other integration types](/payments/online-payments#compare-features-and-availability).

[

Create a Stripe-hosted checkout page

Customers click a button on your site and get redirected to a payment page hosted by Stripe.

](/checkout/quickstart "Create a Stripe-hosted checkout page")

[

Embed a payment form on your site

Embed Stripe’s pre-configured payment form directly in your website without redirecting to Stripe.

](/checkout/embedded/quickstart "Embed a payment form on your site")

[

Build a checkout page with embedded components

Use Elements and the Checkout Sessions API to create a checkout page.

](/checkout/custom/quickstart "Build a checkout page with embedded components")

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/guest-customers

 Guest customers | Stripe Documentation     

[Skip to content](#main-content)

Guest customers

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fguest-customers)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fguest-customers)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

Guest customers

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

Guest customers
===============

Learn how to track the activity of guest customers.
---------------------------------------------------

The [Customer object](/api/customers) represents a customer of your business, and it helps tracking subscriptions and payments that belong to the same customer. Checkout Sessions that don’t create Customers are associated with guest customers instead. Stripe automatically groups [guest customers in the Dashboard](https://dashboard.stripe.com/customers?type=guest) based on them having used the same card, email, or phone to make payments. This unified view helps you review purchasing behavior, refunds, chargebacks, or fraud.

Checkout supports passing in a [customer](/api/checkout/sessions/create#create_checkout_session-customer) to enable you to [prefill customer information](/payments/existing-customers?platform=web&ui=stripe-hosted) on the Checkout page and to associate the payment or subscription with a specific customer.

If you don’t pass in a `customer`, you can set [customer\_creation](/api/checkout/sessions/create#create_checkout_session-customer_creation) to configure whether or not Checkout automatically creates a Customer object when the session is confirmed.

Managing and monitoring guest customers
---------------------------------------

Even though you can’t manage or monitor guest customers in the same way as with Checkout Sessions that create Customers, you can still manage them and monitor their activity.

### Grouping payments under guest customers

We use credit card number as the unique identifier to group credit card payments of your guest customers under the same guest identity. See the [guest customer support page](https://support.stripe.com/questions/guest-customer-faq) for additional details on the matching logic. If the same credit card was used by different guest customers (for example, two spouses using the same credit card to checkout at different times), all guest payments for that credit card show up together under one guest customer. Because we group by credit card, we consider it the same guest customer.

### Updating your privacy policy or other privacy notices

You’re in the best position to know whether this feature is consistent with your privacy policy or other privacy notices. It’s a good practice to review your privacy notices and privacy policy when considering any new feature. Guest customers give you a view of your existing guest data, which can help you better detect fraud and help you manage customer service inquiries.

### Exporting guest customer data from the Dashboard

You can export guest customer data from the [Customers](https://dashboard.stripe.com/customers) tab in the Dashboard. Guest customer information isn’t included in exports from the [Payments](https://dashboard.stripe.com/payments) tab.

### Not seeing any guest customers in the Guests tab

If you don’t see any guest customers under the **Guests** tab, this is because your Stripe integration is passing a Customer ID when creating Checkout Sessions. We only create guest customers for payments without a specific Customer object associated with them.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/build-integration

 Build a checkout page | Documentazione Stripe     

[Passa al contenuto](#main-content)

Panoramica

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fbuild-integration)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fbuild-integration)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

Panoramica

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page

Build a checkout page
=====================

[

CHECKOUT







](/payments/checkout)

Create a payments form and accept payments on your website

Build a Stripe-hosted page, embedded form, or customize your checkout with embedded components with the [Checkout Sessions API](/api/checkout/sessions), which supports one-off payments, subscriptions, and over 40 local payment methods.

[

Quickstart



](/payments/checkout/quickstarts)

![](https://b.stripecdn.com/docs-statics-srv/assets/checkout-card-brand-choice-full-page.9cf891dfb55abcdc9ae9046ea15bc054.png)

If you don’t have a Stripe account, [sign up now](https://dashboard.stripe.com/register/payment_links).

Payment UIs
-----------

You can use three different types of payment UIs with the Checkout Sessions API:

![Hosted checkout form](https://b.stripecdn.com/docs-statics-srv/assets/checkout-hosted-hover.180c6ab2498a8c65daefb5bedae835bf.png)

[Stripe-hosted page](/checkout/quickstart): Customers are redirected to a Stripe-hosted payment page when they’re ready to complete their purchase. After the customer enters their payment details on the payment page and completes the transaction, they can be redirected back to your site.

![Checkout form using Elements with Checkout Sessions API](https://b.stripecdn.com/docs-statics-srv/assets/checkout-embedded-hover.14466c835d9723cfe90b3549956c451a.png)

[Embedded form](/checkout/embedded/quickstart): Customers stay on your site and are shown an embedded form when they’re ready to complete their purchase. The customer enters their payment details on the form and completes the transaction on the same page in your site so they don’t need to be redirected back to your site.

![Checkout form using Elements with Checkout Sessions API](https://b.stripecdn.com/docs-statics-srv/assets/checkout-elements-hover.bfd33fb56dc4ec8915e4ab4601799f49.png)

[Embedded components](/checkout/custom/quickstart): Customizable checkout page built with Stripe Elements. Customers stay on your site and are shown a customized checkout page when they’re ready to complete their purchase.

Compare features and availability
---------------------------------

All integrations support one-time and recurring payments, fraud protection, and [global payments](https://stripe.com/global).

 

[**STRIPE-HOSTED PAGE**](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

[**EMBEDDED FORM**](/payments/accept-a-payment?platform=web&ui=embedded-form)

[**EMBEDDED COMPONENTS**](/checkout/custom/quickstart) Public preview

**UI**

[Checkout](/payments/checkout/how-checkout-works?payment-ui=stripe-hosted)

[Checkout](/payments/checkout/how-checkout-works?payment-ui=embedded-form)

[Elements](/payments/elements)

**API**

[Checkout Sessions](/api/checkout/sessions)

[Checkout Sessions](/api/checkout/sessions)

[Checkout Sessions](/api/checkout/sessions)

**Integration effort**

Low coding

Low coding

More coding

**Hosting**

Stripe-hosted page (optional [custom domains](/payments/checkout/custom-domains))

Embed on your site

Embed on your site

**UI customization**

Limited customization1

Limited customization1

Extensive customization with [Appearance API](/payments/checkout/customization/appearance?payment-ui=embedded-components)

1Limited customization provides [20 preset fonts](/payments/checkout/customization/appearance#font-compatibility), 3 preset border radius options, logo and background customization, and custom button color.

[

Customize look and feel

Customize the appearance and behavior of Checkout.

](/payments/checkout/customization "Customize look and feel")

[

Collect additional information

Collect shipping and other customer info during checkout.

](/payments/checkout/collect-additional-info "Collect additional information")

[

Collect taxes

Learn how to collect taxes for one-time payments in Stripe Checkout.

](/payments/checkout/taxes "Collect taxes")

[

Dynamically update checkout

Make updates while your customer checks out.

](/payments/checkout/dynamic-updates "Dynamically update checkout")

[

Manage your product catalog

Handle your inventory and fulfillment with Checkout.

](/payments/checkout/product-catalog "Manage your product catalog")

[

Subscriptions

Create subscriptions for your customers.

](/payments/subscriptions "Subscriptions")

[

Let customers pay in their local currency

Use Adaptive Pricing to allow customers to pay in their local currency.

](/payments/checkout/adaptive-pricing "Let customers pay in their local currency")

[

Add trials, discounts, upsells, and cross-sells

Add promotions like trials and discounts.

](/payments/checkout/promotions "Add trials, discounts, upsells, and cross-sells")

[

Set up future payments

Save payment details and charge your customers later.

](/payments/checkout/save-and-reuse "Set up future payments")

[

Save payment details during payment

Accept a payment and save your customer’s payment details for future purchases.

](/payments/checkout/save-during-payment "Save payment details during payment")

[

After the payment

Customize the post-payment checkout process.

](/payments/checkout/after-the-payment "After the payment")

[

Migrate payment methods to the Dashboard

](/payments/dashboard-payment-methods "Migrate payment methods to the Dashboard")

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/limit-subscriptions

 Limit customers to one subscription | Documentação da Stripe     

[Pular para o conteúdo](#main-content)

Limitar clientes a uma assinatura

[

Criar conta



](https://dashboard.stripe.com/register)ou[

Entrar



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Flimit-subscriptions)

[

](/)

Pesquise a documentação

/

[Criar conta](https://dashboard.stripe.com/register)

[

Login



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Flimit-subscriptions)

[

Comece já



](/get-started)

[

Pagamentos



](/payments)

[

Automação de finanças



](/finance-automation)

[

Plataformas e marketplaces



](/connect)

[

Banco como serviço



](/financial-services)

[

Ferramentas para desenvolvedores



](/development)

[

Comece já



](/get-started)

[

Pagamentos



](/payments)

[

Automação de finanças



](/finance-automation)

[

Comece já



](/get-started)

[

Pagamentos



](/payments)

[

Automação de finanças



](/finance-automation)

[

Plataformas e marketplaces



](/connect)

[

Banco como serviço



](/financial-services)

APIs e SDKs

Ajuda

[Visão geral](/payments)

Sobre os pagamentos da Stripe

[Atualize sua integração](/payments/upgrades "Melhore sua integração existente")

Análise de pagamentos

Pagamentos online

[Visão geral](/payments/online-payments "Conheça as opções de integração para receber pagamentos online.")[Encontre seu caso de uso](/payments/use-cases/get-started "Saiba como a Stripe pode apoiar a sua empresa.")

Use Payment Links

Crie uma página de checkout

[Visão geral](/payments/checkout/build-integration "Crie uma experiência de pagamentos com o Checkout.")

[Inícios rápidos](/payments/checkout/quickstarts "Comece com um exemplo de código.")

[Personalizar a aparência](/payments/checkout/customization "Controle a aparência da sua página de checkout. O nível de personalização depende do produto que você utiliza.")

[Coletar informações adicionais](/payments/checkout/collect-additional-info "Colete informações como endereços de entrega e números de telefone como parte do processo de checkout.")

[Colete impostos](/payments/checkout/taxes)

[Atualizar checkout dinamicamente](/payments/checkout/dynamic-updates "Faça atualizações enquanto seu cliente faz o checkout.")

[Gerencie seu catálogo de produtos](/payments/checkout/product-catalog)

[Assinaturas](/payments/subscriptions "Gerenciar assinaturas com o Checkout")

[Configurar avaliações gratuitas](/payments/checkout/free-trials)

Limitar clientes a uma assinatura

[Definir data do ciclo de faturamento](/payments/checkout/billing-cycle)

[Gerenciar formas de pagamento](/payments/checkout/payment-methods)

[Permita que os clientes paguem na moeda local](/payments/checkout/adaptive-pricing)

[Adicionar descontos, upsells e vendas cruzadas](/payments/checkout/promotions)

[Configurar pagamentos futuros](/payments/checkout/save-and-reuse "Aprenda a salvar dados do pagamento e cobrar o cliente depois")

[Salvar dados de pagamento durante o pagamento](/payments/checkout/save-during-payment "Salvar dados de pagamento durante o pagamento")

[Após o pagamento](/payments/checkout/after-the-payment)

[Elements com changelog da API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrar do Checkout antigo](/payments/checkout/migration)

[Migrar o Checkout para usar Prices](/payments/checkout/migrating-prices)

Criar uma integração avançada

Crie uma integração no aplicativo

Formas de pagamento

Adicionar formas de pagamento

Gerenciar formas de pagamento

Checkout mais rápido com o Link

IUs de pagamento

Payment Links

Checkout

Web Elements

Elements no aplicativo

Cenários de pagamento

Fluxos de pagamento personalizados

Aquisição flexível

Pagamentos presenciais

Terminal

Outros produtos da Stripe

Financial Connections

Cripto

Climate

Links de repasse

Brasil

Português (Brasil)

[Página inicial](/ "Página inicial")[Pagamentos](/payments "Pagamentos")Build a checkout page[Subscriptions](/payments/subscriptions "Subscriptions")

Limit customers to one subscription
===================================

Direct customers to manage their subscription when they already have one.
-------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

You can redirect customers that already have an active subscription to the [customer portal](/billing/subscriptions/customer-portal "portal de clientes") or your website to manage their subscription. This redirection works with [Checkout](/payments/checkout "Stripe Checkout") (including the [pricing table](/payments/checkout/pricing-table)) and Payment Links.

Stripe uses either the [Customer object](/api/checkout/sessions/object#checkout_session_object-customer) (if you provide it in the Checkout Session) or the email address to detect if a customer already has an active subscription.

![Manage subscription](https://b.stripecdn.com/docs-statics-srv/assets/manage-subscription.47036dfee120d3651fc3819c8b7abfbb.png)

Direct your customers to the customer portal or your website
------------------------------------------------------------

Customer portal

Your website

1.  [Activate the no-code customer portal](/customer-management/activate-no-code-customer-portal) to allow your customers to log in and manage their subscriptions. You need to keep the login link for the customer portal enabled to keep this feature enabled. Disabling the login link disables this feature, which means that customers can create multiple subscriptions.
2.  Enable redirecting your customers to the customer portal in your [Checkout and Payment Links settings](https://dashboard.stripe.com/settings/checkout#subscriptions).

![Subscription settings](https://b.stripecdn.com/docs-statics-srv/assets/subscription-settings.28f8c4efc7a1ca0efceeee8ebeae4786.png)

Active subscription statuses
----------------------------

Active subscriptions have the following [four statuses](/api/subscriptions/object#subscription_object-status):

*   `Active`
*   `PastDue`
*   `Unpaid`
*   `Paused`

Esta página foi útil?

SimNão

Precisa de ajuda? [Fale com o suporte](https://support.stripe.com/).

Participe do nosso [programa de acesso antecipado](https://insiders.stripe.dev/).

Confira o [log de alterações do produto](https://stripe.com/blog/changelog).

Dúvidas? [Fale com a equipe de vendas](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Assine as atualizações para desenvolvedores:

Inscrever-se

Cancele o recebimento quando quiser. Leia a nossa [política de privacidade](https://stripe.com/privacy).

Nesta página

[Direct your customers to the customer portal or your website](#direct-your-customers-to-the-customer-portal-or-your-website "Direct your customers to the customer portal or your website")

[Active subscription statuses](#active-subscription-statuses "Active subscription statuses")

Produtos usados

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

O Stripe Shell oferece uma melhor experiência em desktops.

    $

---

## URL: https://docs.stripe.com/payments/checkout/analyze-conversion-funnel?oo-step=true&should-crawl=true&record-id=1uhahuywh7&wait-before-scraping=2000&save-html=true&save-markdown=true

 Analyze your conversion funnel | Documentazione Stripe     

[Passa al contenuto](#main-content)

Analizzare il funnel di conversione

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fanalyze-conversion-funnel)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fanalyze-conversion-funnel)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Evadere gli ordini](/checkout/fulfillment)

[Send receipts and paid invoices](/payments/checkout/receipts)

[Personalizzare il comportamento di reindirizzamento](/payments/checkout/custom-success-page)

[Recuperare i carrelli abbandonati](/payments/checkout/abandoned-carts)

Analizzare il funnel di conversione

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page[After the payment](/payments/checkout/after-the-payment "After the payment")

Analyze your conversion funnel
==============================

Analyze your Stripe Checkout conversion funnel with Google Analytics 4.
-----------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Use Google Analytics 4 (GA4) to track users as they progress through your Stripe Checkout purchase funnel. Before you begin, set up a [GA4 account](https://support.google.com/analytics/answer/9304153) and add a [GA4 property](https://support.google.com/analytics/answer/9744165?hl=en#zippy=%2Cin-this-article).

Set up your site
----------------

1.  Create a product page with a **Checkout** button:
    
    product.html
    
    `<html>   <head>     <title>Buy cool new product</title>   </head>   <body>     <script>       window.addEventListener("load", function () {         document           .getElementById("submit")           .addEventListener("click", function (event) {             event.preventDefault();             fetch("/create-checkout-session", {               method: "POST",             })               .then((response) => response.json())               .then((checkoutSession) => {                 window.location.href = checkoutSession.url;               });           });       });     </script>     <form>       <button id="submit">Checkout</button>     </form>   </body> </html>`
    
2.  Create a server-side endpoint that creates a Checkout Session and serves the pages:
    
    index.js
    
    ``// This example sets up endpoints using the Express framework. // Watch this video to get started: [https://youtu.be/rPR2aJ6XnAc.](https://youtu.be/rPR2aJ6XnAc)  const express = require("express"); require("dotenv").config();  const app = express();  // Set your secret key. Remember to switch to your live key in production! // See your keys here: [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)  const stripe = require('stripe')(  'sk_test_9W1R4v0cz6AtC9PVwHFzywti'  );  const request = require("request");  app.post(   "/create-checkout-session",   express.urlencoded({ extended: false }),   async (req, res) => {     const session = await stripe.checkout.sessions.  create  ({       payment_method_types: ["card"],       line_items: [         {           price_data: {             currency: "usd",             product_data: {               name: "T-shirt",             },             unit_amount: 2000,           },           quantity: 1,         },       ],       mode: "payment",       success_url: req.get("origin") + "/success",       cancel_url: req.get("origin") + "/cancel",     });      res.json({ url: session.url });   } );  app.get("/product", function (req, res) {   res.sendFile(__dirname + "/product.html"); });  app.get("/success", function (req, res) {   res.sendFile(__dirname + "/success.html"); });  app.get("/cancel", function (req, res) {   res.sendFile(__dirname + "/cancel.html"); });  app.listen(4242, () => console.log(`Listening on port ${4242}!`));``
    
3.  Create a success page:
    
    success.html
    
    `<html>   <head>     <title>Thanks for your order!</title>   </head>   <body>     <h1>Thanks for your order!</h1>     <p>       We appreciate your business! If you have any questions, please email       <a href="mailto:orders@example.com">orders@example.com</a>.     </p>   </body> </html>`
    
4.  Create a canceled page:
    
    canceled.html
    
    `<html>   <head>     <title>Order Canceled!</title>   </head>   <body>     <p>       <a href="/product">Start another order</a>.     </p>   </body> </html>`
    

Instrumentation walkthrough
---------------------------

In the following example, we assume your customer has:

*   Viewed your product page.
*   Clicked the **Buy** button and was redirected to Stripe Checkout.
*   Completed the payment and was redirected to the success page.

### Quick summary

### Add instrumentation

1.  Add `checkout.stripe.com` to your referral exclusion list.
    
2.  Add Google Analytics tags to your product, success, and canceled pages. Tags automatically fire an event on page load.
    
    product.html
    
    `<html>   <head>     <!-- START GOOGLE ANALYTICS -->     <script       async       src="[https://www.googletagmanager.com/gtag/js?id=](https://www.googletagmanager.com/gtag/js?id=)<GOOGLE_ANALYTICS_CLIENT_ID>"     ></script>     <script>       window.dataLayer = window.dataLayer || [];       function gtag() {         window.dataLayer.push(arguments);       }       gtag("js", new Date());       gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");     </script>     <!-- END GOOGLE ANALYTICS -->     <title>Buy cool new product</title>   </head>   <body>     <script>       window.addEventListener("load", function () {         document           .getElementById("submit")           .addEventListener("click", function (event) {             event.preventDefault();             fetch("/create-checkout-session", {               method: "POST",             })               .then((response) => response.json())               .then((checkoutSession) => {                 window.location.href = checkoutSession.url;               });           });       });     </script>     <form>       <button id="submit">Checkout</button>     </form>   </body> </html>`
    
    success.html
    
    `<html>   <head>     <!-- START GOOGLE ANALYTICS -->     <script       async       src="[https://www.googletagmanager.com/gtag/js?id=](https://www.googletagmanager.com/gtag/js?id=)<GOOGLE_ANALYTICS_CLIENT_ID>"     ></script>     <script>       window.dataLayer = window.dataLayer || [];       function gtag() {         window.dataLayer.push(arguments);       }       gtag("js", new Date());       gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");     </script>     <!-- END GOOGLE ANALYTICS -->     <title>Thanks for your order!</title>   </head>   <body>     <h1>Thanks for your order!</h1>     <p>       We appreciate your business! If you have any questions, please email       <a href="mailto:orders@example.com">orders@example.com</a>.     </p>   </body> </html>`
    
    canceled.html
    
    `<html>   <head>     <!-- START GOOGLE ANALYTICS -->     <script       async       src="[https://www.googletagmanager.com/gtag/js?id=](https://www.googletagmanager.com/gtag/js?id=)<GOOGLE_ANALYTICS_CLIENT_ID>"     ></script>     <script>       window.dataLayer = window.dataLayer || [];       function gtag() {         window.dataLayer.push(arguments);       }       gtag("js", new Date());       gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");     </script>     <!-- END GOOGLE ANALYTICS -->     <title>Order Canceled!</title>   </head>   <body>     <p>       <a href="/product">Start another order</a>.     </p>   </body> </html>`
    
3.  Fire an event just before redirecting to Stripe Checkout:
    
    product.html
    
    `<html>   <head>     <!-- START GOOGLE ANALYTICS -->     <script       async       src="[https://www.googletagmanager.com/gtag/js?id=](https://www.googletagmanager.com/gtag/js?id=)<GOOGLE_ANALYTICS_CLIENT_ID>"     ></script>     <script>       window.dataLayer = window.dataLayer || [];       function gtag() {         window.dataLayer.push(arguments);       }       gtag("js", new Date());       gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");     </script>     <!-- END GOOGLE ANALYTICS -->     <title>Buy cool new product</title>   </head>   <body>     <script>       window.addEventListener("load", function () {         document           .getElementById("submit")           .addEventListener("click", function (event) {             event.preventDefault();             fetch("/create-checkout-session", {               method: "POST",             })               .then((response) => response.json())               .then((checkoutSession) => {                 window.location.href = checkoutSession.url;                 gtag("event", "begin_checkout", {                   event_callback: function () {                     window.location.href = checkoutSession.url;                   },                 });               });           });       });     </script>     <form>       <button id="submit">Checkout</button>     </form>   </body> </html>`
    

### Analyze your conversion funnel metrics

After you add the proper instrumentation, you can see the metrics corresponding to each step defined in your conversion funnel:

*   **product page views:** The number of page visitors who viewed the product page.
*   **begin\_checkout event count:** The number of page visitors who clicked the **Buy** button and were redirected to Stripe Checkout.
*   **success page views:** The number of page visitors who completed the purchase and were redirected to the success page.

Using these numbers, you can see where visitors are dropping off in your conversion funnel.

[

FacoltativoServer-side event recording


----------------------------------------





](#server-side-event-recording)

[

FacoltativoLinking client and server-side events


--------------------------------------------------





](#link-client-and-server-side-events)

[

FacoltativoServer-side redirects


----------------------------------





](#server-side-redirect)

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Set up your site](#setup "Set up your site")

[Instrumentation walkthrough](#instrumentation-using-google-analytics "Instrumentation walkthrough")

[Add instrumentation](#adding-instrumentation "Add instrumentation")

[Analyze your conversion funnel metrics](#analysis "Analyze your conversion funnel metrics")

Prodotti utilizzati

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/use-manual-tax-rates

 Use manual Tax Rates | Stripe Documentation     

[Skip to content](#main-content)

Use manual tax rates

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fuse-manual-tax-rates)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fuse-manual-tax-rates)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

Use manual tax rates

[Collect tax IDs](/tax/checkout/tax-ids)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Collect taxes](/payments/checkout/taxes "Collect taxes")

Use manual Tax Rates
====================

Learn how to collect taxes using manual Tax Rates.
--------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Stripe supports manually defining [Tax Rates](/api/tax_rates) to collect taxes (sales, VAT, GST, and others) for different locations. However, [Stripe Tax](/payments/checkout/taxes) is recommended instead of manual tax rates to automatically enable support for 60+ countries.

There are two ways to collect taxes in Checkout:

*   Use _fixed tax rates_ when you know the exact tax rate to charge your customer before they start the checkout process (for example, you only sell to customers in the UK and always charge 20% VAT).
*   Use _dynamic tax rates_ with the Prices API when you need more information from your customer (for example, their billing or shipping address) to determine the tax rate to charge. With dynamic tax rates, you create tax rates for different regions (for example, a 20% VAT tax rate for customers in the UK and a 7.25% sales tax rate for customers in California, US) and Stripe attempts to match your customer’s location to one of those tax rates.

Create tax rates
----------------

First, create tax rates for regions you need to collect taxes for. If you’re working with a small number of tax rates, it’s often simpler to use the [Dashboard](https://dashboard.stripe.com/test/tax-rates) to create and manage them. After creating tax rates, you can pass them as either [fixed](#fixed-tax-rates) or [dynamic tax rates](#dynamic-tax-rates) to the Checkout Session.

#### Create tax rates with the API

The following example demonstrates how you can create a tax rate with the API.

Command Line

cURL

`curl https://api.stripe.com/v1/tax_rates \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d display_name="Sales Tax" \  -d inclusive=false \  -d percentage="7.25" \  -d country=US \  -d state=CA \  -d jurisdiction="US - CA" \  -d description="CA Sales Tax"`

Required properties:

*   The `display_name` is a short-name that describes the specific type of tax, such as `Sales`, `VAT`, or `GST`.
*   The `inclusive` property determines whether the tax `percentage` is either added to, or included in, the overall amount.
*   The `percentage` is a number (up to 4 decimal places) that represents the tax percentage to be collected.

Optional properties:

*   The optional `country` property is a valid [two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm). Some countries (for example, United States) require an additional two-letter `state` property. Use these properties to apply dynamic tax rates based on your customer’s billing or shipping address in Checkout Sessions.
    
*   The optional `jurisdiction` property represents the tax rate’s tax jurisdiction and you can use it to differentiate between tax rates of the same percentage. In the Dashboard, jurisdiction appears as the tax rate’s _Region_ label.
    
*   You can also store additional details in the `description`. This property isn’t exposed to your customers.
    

#### Note

The `percentage`, `country`, and `state` properties are immutable and can only be set when you create the tax rate. This is to ensure existing subscriptions and invoices using tax rates are not affected. If you need to update these properties, create a new tax rate and archive the old object.

Fixed tax rates
---------------

*   For one-time payments, pass the Tax Rate ID to [line\_item.tax\_rates](/api/checkout/sessions/create#create_checkout_session-line_items-tax_rates).
*   For recurring payments, pass the Tax Rate ID to [subscription\_data.default\_tax-rates](/api/checkout/sessions/create#create_checkout_session-subscription_data-default_tax_rates).

One-time payments

Recurring payments

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "line_items[0][tax_rates][0]"=  {{TAX_RATE_ID}}   \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

Dynamic tax rates
-----------------

Pass the array of tax rates to [line\_items.dynamic\_tax\_rates](/api/checkout/sessions/create#create_checkout_session-line_items-dynamic_tax_rates). Each tax rate must have a [supported country](/api/checkout/sessions/create#create_checkout_session-line_items-dynamic_tax_rates), and for the US, a `state`. The current list of supported countries are:

*   Austria
    
*   Australia
    
*   Belgium
    
*   Bulgaria
    
*   Cyprus
    
*   Czech Republic
    
*   Germany
    
*   Denmark
    
*   Estonia
    
*   Spain
    
*   Finland
    
*   France
    
*   United Kingdom
    
*   Greece
    
*   Croatia
    
*   Hungary
    
*   Ireland
    
*   Italy
    
*   Lithuania
    
*   Luxembourg
    
*   Latvia
    
*   Malta
    
*   Netherlands
    
*   Poland
    
*   Portugal
    
*   Romania
    
*   Sweden
    
*   Slovenia
    
*   Slovakia
    
*   United States
    

This list matches tax rates to your customer’s [shipping address](/payments/collect-addresses?payment-ui=checkout) or billing address. The shipping address takes precedence over the billing address for determining the tax rate to charge.

Billing address collection is automatically enabled when using dynamic tax rates. If you’re not collecting a shipping address, your customer’s billing address is used to determine the tax rate. If you haven’t passed a tax rate that matches your customer’s shipping or billing address, no tax rate is applied.

#### Common mistake

[line\_items.tax\_rates](/api/checkout/sessions/create#create_checkout_session-line_items-tax_rates) can’t be used in combination with [line\_items.dynamic\_tax\_rates](/api/checkout/sessions/create#create_checkout_session-line_items-dynamic_tax_rates).

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=2 \  -d "line_items[0][dynamic_tax_rates][0]"={{FIRST_TAX_RATE_ID}} \   -d "line_items[0][dynamic_tax_rates][1]"={{SECOND_TAX_RATE_ID}} \   -d mode=payment \   --data-urlencode success_url="https://example.com/success" \   --data-urlencode cancel_url="https://example.com/cancel"`

### Apple Pay and Google Pay

When using dynamic tax rates without [shipping\_address\_collection](/api/checkout/sessions/create#create_checkout_session-shipping_address_collection), Apple Pay and Google Pay aren’t available to customers.

Tax reporting and remittance
----------------------------

Any business collecting taxes ultimately needs to remit tax to the appropriate government. You can use Stripe’s data exports to populate the periodic reports that you’re required to make to taxation authorities.

### Data exports

From the Dashboard’s [Tax Rates list](https://dashboard.stripe.com/test/tax-rates/), you can export data files required for tax reporting calculations. Different Checkout modes require different processes.

#### Payment mode

When using Checkout in payment mode, use the following two tax reporting exports:

*   **Checkout payment mode line item tax export**—Includes details down to the line-item level, including per-line-item tax rates, inclusive and exclusive, amounts, and so on. This is a lower-level export.
*   **Checkout payment mode totals export**—Shows the aggregate tax collected on the Checkout Session as a whole, including adjustments for any refunds.

For remittance reporting, use the Checkout payment mode line item tax export to sum all of the amounts paid for all of the tax rates used. To factor in any refunds, you also need to pivot against the Checkout payment mode totals export.

#### Subscription mode

When using Checkout in subscription mode, use the [Stripe Billing tax exports](/billing/taxes/tax-rates#remittance) instead.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Create tax rates](#create-tax-rates "Create tax rates")

[Fixed tax rates](#fixed-tax-rates "Fixed tax rates")

[Dynamic tax rates](#dynamic-tax-rates "Dynamic tax rates")

[Apple Pay and Google Pay](#apple-pay-and-google-pay "Apple Pay and Google Pay")

[Tax reporting and remittance](#remittance "Tax reporting and remittance")

[Data exports](#data-exports "Data exports")

Products Used

[

Checkout





](/payments/checkout)

[

Tax





](/tax)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/managing-limited-inventory

 Manage limited inventory | Stripe Documentation     

[Skip to content](#main-content)

Manage limited inventory

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmanaging-limited-inventory)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmanaging-limited-inventory)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

Manage limited inventory

[Make line item quantities adjustable](/payments/checkout/adjustable-quantity)

[Let customers decide what to pay](/payments/checkout/pay-what-you-want)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Manage your product catalog](/payments/checkout/product-catalog "Manage your product catalog")

Manage limited inventory
========================

Prevent customers from holding inventory in carts by expiring Checkout Sessions.
--------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

For some types of limited-inventory businesses, it’s necessary to prevent customers from reserving items for a long time without completing the purchase. For example, an event ticket seller wants to allow customers only a few minutes to buy their selected tickets before cancelling the sale and making those tickets available again. You can cancel a pending sale by expiring the [Checkout Session](/api/checkout/sessions "checkout session").

Checkout supports both manual and timed session expiration. When a Checkout Session expires, its [status property](/api/checkout/sessions/object#checkout_session_object-status) changes to `expired`.

Manual expiration
-----------------

To immediately expire an open Checkout Session and cancel any pending purchase, use the [expire](/api/checkout/sessions/expire) endpoint.

Command Line

Select a languagecURL

`curl -X POST https://api.stripe.com/v1/checkout/sessions/  {{SESSION_ID}}  /expire \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :"`

Set an expiration time
----------------------

When you create a Checkout Session, specify an expiration timestamp by setting the [expires\_at](/api/checkout/sessions/create#create_checkout_session-expires_at) parameter. The value must be between 30 minutes and 24 hours after the current time. If you don’t specify `expires_at`, the default value is 24 hours after the current time.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \   -u sk_test_4eC39HqLyjWDarjtT1zdp7dc  : \   -d customer=  {{CUSTOMER_ID}}   \   -d "line_items[0][price]"=  {{PRICE_ID}}   \   -d "line_items[0][quantity]"=1 \   -d mode=payment \   -d success_url="https://example.com/success" \   -d expires_at="{{NOW_PLUS_TWO_HOURS}}"`

Return items to your inventory
------------------------------

When a [Checkout Session](/api/checkout/sessions) expires, Stripe sends the `checkout.session.expired` event. Configure your webhook endpoint to listen for this event so your webhook handler can return to inventory any items reserved in the expired session. For more information, see [Expire a Session](/api/checkout/sessions/expire).

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Manual expiration](#manual-expiration "Manual expiration")

[Set an expiration time](#setting-an-expiration-time "Set an expiration time")

[Return items to your inventory](#return-items-to-your-inventory "Return items to your inventory")

Products Used

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/custom-success-page

 Customize redirect behavior | Stripe Documentation     

[Skip to content](#main-content)

Customize redirect behavior

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-success-page)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-success-page)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Fulfill orders](/checkout/fulfillment)

[Send receipts and paid invoices](/payments/checkout/receipts)

Customize redirect behavior

[Recover abandoned carts](/payments/checkout/abandoned-carts)

[Analyze conversion funnel](/payments/checkout/analyze-conversion-funnel)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Netherlands

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[After the payment](/payments/checkout/after-the-payment "After the payment")

Customize redirect behavior
===========================

Display a confirmation page with your customer's order information.
-------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

If you have a Checkout integration that uses a Stripe-hosted page, Stripe redirects your customer to a success page that you create and host on your site. You can use the details from a [Checkout Session](/api/checkout/sessions) to display an order confirmation page for your customer (for example, their name or payment amount) after the payment.

Redirect customers to a success page
------------------------------------

To use the details from a Checkout Session:

1.  Modify the [success\_url](/api/checkout/sessions/create#create_checkout_session-success_url) to pass the Checkout Session ID to the client side.
2.  Look up the Checkout Session using the ID on your success page.
3.  Use the Checkout Session to customize what’s displayed on your success page.

Modify the success URL Server-side
----------------------------------

Add the `{CHECKOUT_SESSION_ID}` template variable to the `success_url` when you create the Checkout Session. Note that this is a literal string and must be added exactly as you see it here. Do not substitute it with a Checkout Session ID—this happens automatically after your customer pays and is redirected to the success page.

Ruby

`session = Stripe::Checkout::Session.  create  (   success_url: "[http://yoursite.com/order/success](http://yoursite.com/order/success)",   success_url: "[http://yoursite.com/order/success?session_id={CHECKOUT_SESSION_ID}](http://yoursite.com/order/success?session_id={CHECKOUT_SESSION_ID})",   # other options..., )`

Create the success page Server-side
-----------------------------------

Look up the Checkout Session using the ID and create a success page to display the order information. This example prints out the customer’s name:

Ruby

`# This example sets up an endpoint using the Sinatra framework. # Watch this video to get started: [https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)  # Set your secret key. Remember to switch to your live secret key in production. # See your keys here: [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys) Stripe.api_key =   'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'  require 'sinatra'  get '/order/success' do   session = Stripe::Checkout::Session.retrieve(params[:session_id])   customer = Stripe::Customer.retrieve(session.customer)    "<html><body><h1>Thanks for your order, #{customer.name}!</h1></body></html>" end`

Test the integration
--------------------

To confirm that your redirect is working as expected:

1.  Click the checkout button.
2.  Fill in the customer name and other payment details.
3.  Click **Pay**.

If it works, you’re redirected to the success page with your custom message. For example, if you used the message in the code samples, the success page displays this message: **Thanks for your order, Jenny Rosen!**

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Redirect customers to a success page](#success-url "Redirect customers to a success page")

[Modify the success URL](#modify-the-success-url "Modify the success URL")

[Create the success page](#create-the-success-page "Create the success page")

[Test the integration](#test-the-integration "Test the integration")

Products Used

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/adjustable-quantity

 Make line item quantities adjustable | Stripe Documentation     

[Skip to content](#main-content)

Make line item quantities adjustable

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fadjustable-quantity)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fadjustable-quantity)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Manage limited inventory](/payments/checkout/managing-limited-inventory)

Make line item quantities adjustable

[Let customers decide what to pay](/payments/checkout/pay-what-you-want)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Poland

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Manage your product catalog](/payments/checkout/product-catalog "Manage your product catalog")

Make line item quantities adjustable
====================================

Enable your customers to adjust the quantity of items during checkout.
----------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

The line items for each [Checkout Session](/api/checkout/sessions) keep track of what your customer is purchasing. You can configure the Checkout Session so customers can adjust line item quantities during checkout.

Create a Checkout Session with an adjustable quantity
-----------------------------------------------------

Set `adjustable_quantity` on your `line_items` when creating a Checkout Session to enable your customers to update the quantity of an item during checkout.

You can customize the default settings for the minimum and maximum quantities allowed by setting `adjustable_quantity.minimum` and `adjustable_quantity.maximum`. By default, an item’s minimum adjustable quantity is `0` and the maximum adjustable quantity is `99`. You can specify a value of up to `999999` for `adjustable_quantity.maximum`.

When using adjustable quantities with a `line_items[].quantity` value greater than `99` (the default adjustable maximum), set `adjustable_quantity.maximum` to be greater than or equal to that item’s quantity.

If you use adjustable quantities, change your configuration so that it uses `adjustable_quantity.maximum` when creating the Checkout Session to reserve inventory quantity instead of the `line_items` quantity.

Checkout prevents the customer from removing an item if it is the only item remaining.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_7mJuPfZsBzc3JkrANrFrcDqC  :" \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][unit_amount]"=2000 \  -d "line_items[0][price_data][tax_behavior]"=exclusive \  -d "line_items[0][adjustable_quantity][enabled]"=true \  -d "line_items[0][adjustable_quantity][minimum]"=1 \  -d "line_items[0][adjustable_quantity][maximum]"=10 \  -d "line_items[0][quantity]"=1 \  -d "automatic_tax[enabled]"=true \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

Handle completed transactions
-----------------------------

After the payment completes, you can make a request for the finalized [line items](/api/checkout/sessions/line_items) and their quantities. If your customer removes a line item, it is also removed from the line items response. See the [Fulfillment guide](/checkout/fulfillment) to learn how to create an event handler to handle completed Checkout Sessions.

#### Note

To test your event handler, [install the Stripe CLI](/stripe-cli) and use `stripe listen --forward-to localhost:4242/webhook` to [forward events to your local server](/webhooks#test-webhook).

Ruby

``# Set your secret key. Remember to switch to your live secret key in production! # See your keys here: [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys) Stripe.api_key =   "sk_test_7mJuPfZsBzc3JkrANrFrcDqC"  require 'sinatra'  # You can find your endpoint's secret in your webhook settings endpoint_secret = 'whsec_...'  post '/webhook' do   event = nil    # Verify webhook signature and extract the event   # See [https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events) for more information.   begin     sig_header = request.env['HTTP_STRIPE_SIGNATURE']     payload = request.body.read     event = Stripe::Webhook.construct_event(payload, sig_header, endpoint_secret)   rescue JSON::ParserError => e     # Invalid payload     return status 400   rescue Stripe::SignatureVerificationError => e     # Invalid signature     return status 400   end    if event['type'] == 'checkout.session.completed'     checkout_session = event['data']['object']      line_items = Stripe::Checkout::Session.list_line_items(checkout_session['id'], {limit: 100})      # Fulfill the purchase...     begin       fulfill_order(checkout_session, line_items)     rescue NotImplementedError => e       return status 400     end   end    status 200 end  def fulfill_order(checkout_session, line_items)   # TODO: Remove error and implement...   raise NotImplementedError.new(<<~MSG)     Given the Checkout Session "#{checkout_session.id}" load your internal order from the database here.     Then you can reconcile your order's quantities with the final line item quantity purchased. You can use `checkout_session.metadata` and `price.metadata` to store and later reference your internal order and item ids.   MSG end``

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Create a Checkout Session with an adjustable quantity](#enable-adjustable-quantity "Create a Checkout Session with an adjustable quantity")

[Handle completed transactions](#handling-transactions "Handle completed transactions")

Products Used

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/customization

 Personalizzare Checkout | Documentazione Stripe     

[Passa al contenuto](#main-content)

Personalizzare l'aspetto

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

Personalizzare l'aspetto

[Personalizza l'aspetto](/payments/checkout/customization/appearance)

[Personalizza il testo e le politiche](/payments/checkout/customization/policies)

[Personalizzare la procedura](/payments/checkout/customization/behavior)

[Utilizzare il dominio personalizzato](/payments/checkout/custom-domains)

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page

Personalizzare Checkout
=======================

Personalizza l'aspetto e il comportamento di Checkout.
------------------------------------------------------

Personalizza Checkout con branding, politiche legali e di reso, compilazione automatica dei pagamenti dei clienti e domini personalizzati.

[

Aspetto

Personalizza l’aspetto della tua pagina di Checkout, includendo il branding.

](/payments/checkout/customization/appearance "Aspetto")

[

Testo e politiche

Personalizza le informazioni di contatto dell’assistenza, le politiche e altri testi che i clienti visualizzano.

](/payments/checkout/customization/policies "Testo e politiche")

[

Esperienza di pagamento

Personalizza il comportamento di Checkout per ottimizzare la conversione e aumentare i ricavi.

](/payments/checkout/customization/behavior "Esperienza di pagamento")

[

Utilizzare il dominio personalizzato

Trasferisci il tuo dominio personalizzato su Stripe Checkout, Payment Links e sul portale cliente.

](/payments/checkout/custom-domains "Utilizzare il dominio personalizzato")

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/customization/behavior

 Customize checkout behavior | Documentazione Stripe     

[Passa al contenuto](#main-content)

Personalizzare la procedura

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fbehavior)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fbehavior)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Personalizza l'aspetto](/payments/checkout/customization/appearance)

[Personalizza il testo e le politiche](/payments/checkout/customization/policies)

Personalizzare la procedura

[Utilizzare il dominio personalizzato](/payments/checkout/custom-domains)

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page[Customize look and feel](/payments/checkout/customization "Customize look and feel")

Customize checkout behavior
===========================

Customize the behavior of the checkout process to increase conversion and revenue.
----------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Customize the Submit button
---------------------------

To better align Checkout with your business model, configure the copy displayed on the Checkout submit button for one-time purchases.

Define a `submit_type` on your session. In this example (for a 5 USD donation), your customized Checkout submit button would read **Donate $5.00**. See the [API reference](/api/checkout/sessions/create#create_checkout_session-submit_type) for a complete list of `submit_type` options.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d submit_type=donate \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

Localization and supported languages
------------------------------------

By default, Checkout detects the locale of the customer’s browser and displays a translated version of the page in their language, if Stripe [supports it](https://support.stripe.com/questions/supported-languages-for-stripe-checkout). You can override the browser locale for Checkout by passing the `locale` [parameter](/api/checkout/sessions/create#create_checkout_session-locale) when you create a Checkout Session.

Checkout also uses the locale to format numbers and currencies. For example, when selling a product whose price is set in EUR with the locale set to `auto`, a browser configured to use English (`en`) would display €25.00 while one configured for German (`de`) would display 25,00 €.

Autofill payment details with Link
----------------------------------

You can automatically use Link (Stripe’s one-click checkout) in your prebuilt Checkout page. To learn more, see [Link with Checkout](/payments/link/checkout-link).

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Customize the Submit button](#submit-button "Customize the Submit button")

[Localization and supported languages](#localization "Localization and supported languages")

[Autofill payment details with Link](#link "Autofill payment details with Link")

Prodotti utilizzati

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/cross-sells

 Cross-sells | Documentazione Stripe     

[Passa al contenuto](#main-content)

Configurare cross-selling

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcross-sells)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcross-sells)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Aggiungere sconti](/payments/checkout/discounts)

[Configurare le vendite extra di abbonamenti](/payments/checkout/upsells)

Configurare cross-selling

[Consentire ai clienti di completare gli ordini gratuitamente](/payments/checkout/no-cost-orders)

[Visualizzare i prezzi annuali nei termini mensili](/payments/checkout/yearly-price-display)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page[Add discounts, upsells, and cross-sells](/payments/checkout/promotions "Add discounts, upsells, and cross-sells")

Cross-sells
===========

Enable customers to purchase complementary products at checkout by using cross-sells.
-------------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

![Cross-sell product in Checkout](https://b.stripecdn.com/docs-statics-srv/assets/cross-sell-session.32236b96e980634a6c0060050eea5dbf.png)

A cross-sell is a product that you can add to an order using Checkout.

Cross-sells enable customers to optionally purchase other related products using Checkout. Cross-sells can increase your average order value and revenue. For Checkout to offer a product as a cross-sell, the product must meet the following criteria:

*   The product must be associated with only a single [Price](/api/prices/object#price_object-product).
*   The [currency](/api/prices/object#price_object-currency) of the cross-sell product’s price must match the currency of the other prices in the Checkout Session.
*   If the cross-sell product’s price [type](/api/prices/object#price_object-type) is `recurring`, the Checkout Session must be in subscription mode and its recurring interval must match the recurring interval of the other prices in the Checkout Session.
*   If you’re using [subscription upsells](/payments/checkout/upsells), cross-sells only support products with non-recurring prices. For example, you can cross-sell a one-time setup fee while also upselling a monthly subscription to annual billing.
*   If you’re using [automatic taxes](/tax), cross-sells only support products with prices with specified [tax behavior](/tax/products-prices-tax-codes-tax-behavior#tax-behavior). You can either [set tax behavior for a price](/tax/products-prices-tax-codes-tax-behavior#setting-tax-behavior-on-a-price-(optional)) or set the default tax behavior for all prices under [Tax Settings](https://dashboard.stripe.com/test/settings/tax) in the Stripe Dashboard.

Create a cross-sell
-------------------

![Configure a cross-sell on the Product detail page](https://b.stripecdn.com/docs-statics-srv/assets/add-cross-sell.685564769c217a27f88b9ab9605d9c65.gif)

Configure a cross-sell on the Product detail page.

You can configure a cross-sell in the [Dashboard](https://dashboard.stripe.com/products?active=true) on the Product details page. Visit the Product details page for the product from which you want to cross-sell another complementary product. You’ll see a **Cross-sells** section with a dropdown menu containing your other Products. Select a Product with a single Price. After you configure it, all eligible Checkout Sessions cross-sell the product selected from the dropdown menu. For example, a customer purchasing a ‘Togethere Professional’ subscription would be cross-sold the ‘Professional Services: Deployment’ product.

Checkout flow
-------------

In Checkout, buyers see an option to add the cross-sell to their purchase. If buyers add the cross-sell to the Checkout Session, they can also remove it. If they remove it, the option to add the cross-sell appears again.

#### Nota

The quantity of cross-sell line items cannot be adjusted. The current maximum is 1.

![Customer preview of a cross-sell on the Product detail page](https://b.stripecdn.com/docs-statics-srv/assets/cross-sell-preview.cc9b1a4716015a18004f62de760cf29a.gif)

Customer preview.

Retrieve Checkout Session line items
------------------------------------

After a customer adds a cross-sell, the `line_items` for the Checkout Session update to reflect the addition. When [fulfilling your order](/checkout/fulfillment#create-payment-event-handler) using the `checkout.session.completed` webhook, make sure to [retrieve the line items](/api/checkout/sessions/line_items).

Remove a cross-sell
-------------------

You can remove a cross-sell on the Product details page. After you remove it, the product won’t be offered to any new Checkout Sessions.

![Remove a cross-sell from the Product detail page](https://b.stripecdn.com/docs-statics-srv/assets/remove-cross-sell.a08765b1278a8187c282964f89641b92.gif)

Remove a cross-sell.

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Create a cross-sell](#create-cross-sell "Create a cross-sell")

[Checkout flow](#checkout-flow "Checkout flow")

[Retrieve Checkout Session line items](#line-items "Retrieve Checkout Session line items")

[Remove a cross-sell](#remove-cross-sell "Remove a cross-sell")

Prodotti utilizzati

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/adaptive-pricing

 Adaptive Pricing | Stripe Documentation     

[Skip to content](#main-content)

Let customers pay in their local currency

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fadaptive-pricing)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fadaptive-pricing)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

Let customers pay in their local currency

[Define manual currency prices](/payments/checkout/manual-currency-prices)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

Adaptive Pricing
================

Let customers pay in their local currency with Adaptive Pricing to increase international revenue.
--------------------------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Private preview

Adaptive Pricing lets your customers pay in their local currency in more than [150 countries](#supported-currencies). With Adaptive Pricing, Stripe automatically calculates the localized price and handles all currency conversion. The presentment currency is inferred from the buyer’s public IP address. Enabling Adaptive Pricing can increase conversion rates from global buyers and increase international revenue.

Use Adaptive Pricing to:

*   Display pricing in local currencies based on location
*   Calculate prices in real-time using an exchange rate guaranteed for 24 hours
*   Unlock payment methods that require local currency
*   Facilitate your compliance when presenting supported currencies

![A customer in France views a price localized from USD to EUR](https://b.stripecdn.com/docs-statics-srv/assets/adaptive_pricing.7955669ffbb4f3ddeaca083e186eeb99.png)

### Integration effort

Low code

### Fees

View information on [fees and our FAQ](https://support.stripe.com/questions/adaptive-pricing).

[

Enable Adaptive Pricing

Dashboard




--------------------------------------





](#enable-adaptive-pricing)

Enable Adaptive Pricing in your [payment settings](https://dashboard.stripe.com/settings/adaptive-pricing) in the Dashboard. You can enable Adaptive Pricing in test mode and live mode. Disabling Adaptive Pricing doesn’t affect Checkout Sessions that have already been converted.

Adaptive Pricing works with Checkout, Payment Links, pricing tables, and local payment methods.

[

Configure local payment methods

Dashboard




----------------------------------------------





](#configure-local-payment-methods)

You can configure which payment methods you accept in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). Adaptive Pricing can increase the usage of local payment methods by ensuring customers have the option to pay in their currency and with payment methods most relevant to them. As an example, 70% of all e-commerce transactions in the Netherlands use iDEAL, but it only works with EUR. Adaptive Pricing enables the following payment methods:

*   Alipay
    
*   Bancontact
    
*   BLIK
    
*   Canadian pre-authorized debit
    
*   EPS
    
*   iDEAL
    
*   PayPal
    
*   P24
    
*   SEPA Debit
    
*   Sofort
    
*   Swish
    
*   WeChat Pay
    

[

Event destinations and reporting

Server-side




-------------------------------------------------





](#event-destinations-reporting)

Enabling Adaptive Pricing can affect some parts of your integration, such as event destinations and reporting. Review your integration to make sure any [event destinations](#event-destinations-reporting) can handle PaymentIntent objects with local currencies.

*   Use the [currency\_conversion](/api/checkout/sessions/object#checkout_session_object-currency_conversion) hash on the Checkout Session object to determine what your customer would have paid in the default currency.
*   Use the [BalanceTransactions API](/api/balance_transactions) to determine how much you receive after fees.

Depending on the user-selected currency, both the Checkout Session and the underlying PaymentIntent objects update automatically to reflect the selected currency and amount. After a user pays in local currency, the Checkout Session object’s currency and total amount is in local currency and contains a `currency_conversion` hash to reflect what the user would have paid in the default currency. Learn more about what’s [deposited in your account after fees](/api/balance_transactions).

The [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event contains a `currency_conversion` hash that includes the `amount_total` and `amount_subtotal` in the `source_currency`. The amounts reflect what your customer would have paid in the source currency.

`{   "id":   '{{EVENT_ID}}'  ,   "object": "event",   "type": "checkout.session.completed",   "data": {     "object": {       "id":   '{{SESSION_ID}}'  ,       "object": "checkout.session",       "currency": "cad",       "amount_total": 2055,       "amount_subtotal": 2055,       "currency_conversion": {         "amount_subtotal": 1500,         "amount_total": 1500,         "source_currency": "usd",         "fx_rate": "1.37"       }     }   } }`

[

Testing


---------





](#testing)

To test local currency presentment for Checkout, Payment Links, and the [pricing table](/payments/checkout/pricing-table), pass in a location-formatted customer email that includes a suffix in a `+location_XX` format in the local part of the email. `XX` must be a valid [two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm).

For example, to test currency presentment for a customer in France, pass in an email like `test+location_FR@example.com`.

When you visit the URL for a Checkout Session, Payment Link, or pricing table created with a location-formatted email, you see the same currency as a customer does in the specified country.

### Testing Checkout

When you create a Checkout Session, pass the location-formatted email as [customer\_email](/api/checkout/sessions/object#checkout_session_object-customer_email) to simulate Checkout from a particular country.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u   sk_test_4eC39HqLyjWDarjtT1zdp7dc  : \   -d "line_items[0][price]"="{{PRICE_ID}}" \  -d "line_items[0][quantity]"=1 \  -d mode=payment \  -d success_url="https://example.com/success" \   --data-urlencode customer_email="test+location_FR@example.com"`

You can also create a [Customer](/api/customers/create) and specify their email that contains the `+location_XX` suffix. Stripe test cards work as usual.

When it’s possible to present the customer’s local currency in Checkout, the [Checkout Session](/api/checkout/sessions/object) object changes. Fields like `currency`, `payment_method_types`, and `amount_total` reflect the local currency and price.

### Testing Payment Links

For Payment Links, pass the location-formatted email as the `prefilled_email` [URL parameter](/payment-links/customize#customize-checkout-with-url-parameters) to test currency presentment for customers in different countries.

### Testing Pricing table

For the pricing table, pass the location-formatted email as the [customer-email](/payments/checkout/pricing-table#customer-email) attribute to test currency presentment for customers in different countries.

Supported currencies
--------------------

Businesses in supported regions can automatically convert prices to the local currencies of their customers in the following markets:

### North America

### South America

### Europe

### Asia

### Oceania

### Africa

Restrictions
------------

Adaptive Pricing doesn’t currently work with Connect or Elements with the Payment Intents API.

Additionally, Adaptive Pricing requires the [currency for your prices](/api/checkout/sessions/object#checkout_session_object-currency) to be the same as your default settlement currency. Prices automatically convert during checkout. This applies to [prices](/products-prices/manage-prices#prices-create) you create and reference with a price ID and prices you create inline with [price\_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data) when you create a Checkout Session.

Adaptive Pricing doesn’t apply for Checkout Sessions that:

*   Contain explicitly defined [manual currency prices](/payments/checkout/manual-currency-prices).
*   Are in `subscription` mode.
*   Use Connect parameters like `application_fee_amount`, `on_behalf_of`, and `transfer_data`.
*   Use [capture\_method](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method) as `manual`.
*   Set the [currency](/api/checkout/sessions/create#create_checkout_session-currency) value on creation.
*   Use [custom amounts](/payments/checkout/pay-what-you-want).
*   Present the customer a local currency that is also configured as a [settlement currency](/payouts#supported-accounts-and-settlement-currencies). For example, suppose an account settles in both `EUR` and `GBP`. If they price in `EUR`, customers with local currency `GBP` don’t see Adaptive Pricing. Customers with a local currency other than `EUR` or `GBP`, such as `JPY`, see Adaptive Pricing.

Checkout Sessions that aren’t supported by Adaptive Pricing present prices in the original currency that you’ve set your prices in.

Pricing
-------

*   You pay 0%
*   Your buyers pay 2-4%

You (the business) don’t directly pay any additional fees for Adaptive Pricing, as all such fees are paid for by your customers. Stripe applies a conversion fee of between 2-4% to the exchange rate you present to your customers, increasing their purchase price by a corresponding amount. The fee applied is determined by Stripe and varies for the purposes of increasing customer conversion. Stripe typically charges a fee of 4% for orders under 500 USD, 3% for 500–1,500 USD, and 2% for orders over 1,500 USD. For detailed information about current Stripe fees, see our [pricing page](https://stripe.com/pricing).

Exchange rate
-------------

Stripe uses the mid-market exchange rate and applies a fee to guarantee the rate for the duration of the Checkout Session (up to 24 hours) through settlement. If the exchange rate changes by more than 5% in that time, Stripe might use the updated exchange rate to calculate your payout.

Learn more about how Stripe handles [currency conversions](/currencies/conversions) and [Adaptive Pricing fees](https://support.stripe.com/questions/adaptive-pricing#:~:text=Adaptive%20Pricing%20is%20a%20Checkout,latest%20Stripe%2Dprovided%20exchange%20rates).

Refunds
-------

Stripe pays out refunds in the currency your customer pays in using the latest Stripe-provided exchange rate. This means that you might pay more or less to cover the refund depending on how the exchange rate changes.

### Example refund

We ignore Stripe fees in this example for simplicity. Suppose:

1.  You’re a US business that uses Checkout to sell a product for 100 USD and have activated Adaptive Pricing.
2.  A customer in Canada views your Checkout page, sees the localized price of 137 CAD at an exchange rate of 1.37 CAD per 1 USD, and completes the purchase.
3.  Stripe processes the payment, converting the 137 CAD to 100 USD to pay you in your settlement currency.
4.  Later, when the exchange rate has changed to 1.40 CAD per 1 USD, you issue a full refund to the customer.
5.  Stripe deducts 97.86 USD from your account, exchanging it at 1.40 CAD per 1 USD to pay out the 137 CAD refund.

Learn more about how Stripe helps you manage [refunds](/refunds).

See also
--------

*   [Adaptive Pricing FAQ](https://support.stripe.com/questions/adaptive-pricing)

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Enable Adaptive Pricing](#enable-adaptive-pricing "Enable Adaptive Pricing")

[Configure local payment methods](#configure-local-payment-methods "Configure local payment methods")

[Event destinations and reporting](#event-destinations-reporting "Event destinations and reporting")

[Testing](#testing "Testing")

[Testing Checkout](#testing-checkout "Testing Checkout")

[Testing Payment Links](#testing-payment-links "Testing Payment Links")

[Testing Pricing table](#testing-pricing-table "Testing Pricing table")

[Supported currencies](#supported-currencies "Supported currencies")

[Restrictions](#restrictions "Restrictions")

[Pricing](#pricing "Pricing")

[Exchange rate](#exchange-rate "Exchange rate")

[Refunds](#refunds "Refunds")

[Example refund](#example-refund "Example refund")

[See also](#see-also "See also")

Products Used

[

Checkout





](/payments/checkout)

[

Elements





](/payments/elements)

[

Payment Links





](/payments/payment-links)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/discounts

 Add discounts | Stripe Documentation     

[Skip to content](#main-content)

Add discounts

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fdiscounts)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fdiscounts)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

Add discounts

[Configure subscription upsells](/payments/checkout/upsells)

[Configure cross-sells](/payments/checkout/cross-sells)

[Let customers complete orders for free](/payments/checkout/no-cost-orders)

[Display yearly prices in monthly terms](/payments/checkout/yearly-price-display)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Add discounts, upsells, and cross-sells](/payments/checkout/promotions "Add discounts, upsells, and cross-sells")

Add discounts
=============

Reduce the amount charged to a customer by discounting their subtotal with coupons and promotion codes.
-------------------------------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

You can use discounts to reduce the amount charged to a customer. Coupons and promotion codes allow you to:

*   Apply a discount to an entire purchase subtotal
*   Apply a discount to specific products
*   Reduce the total charged by a percentage or a flat amount
*   Create customer-facing promotion codes on top of coupons to share directly with customers

#### Note

To use coupons for discounting [subscriptions](/billing/subscriptions/creating "subscriptions") with Checkout and Billing, see [Discounts for subscriptions](/billing/subscriptions/coupons).

Create a coupon
---------------

Coupons specify a fixed value discount. You can create customer-facing promotion codes that map to a single underlying coupon. This means that the codes `FALLPROMO` and `SPRINGPROMO` can both point to one 25% off coupon. You can create coupons in the [Dashboard](https://dashboard.stripe.com/coupons) or with the [API](/api#coupons):

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/coupons \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d percent_off=20 \  -d duration=once`

Use a coupon
------------

To create a session with an applied discount, pass the [coupon ID](/api/coupons/object#coupon_object-id) in the `coupon` parameter of the [discounts](/api/checkout/sessions/create#create_checkout_session-discounts) array. Checkout currently supports up to one coupon or promotion code.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "discounts[0][coupon]"=  {{COUPON_ID}}   \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

Configure a coupon
------------------

Coupons have the following parameters that you can use:

*   `currency`
*   `percent_off` or `amount_off`
*   `max_redemptions`
*   `redeem_by`, the latest date customers can apply the coupon
*   `applies_to`, limits the products that the coupon applies to

#### Note

The coupon object adds discounts to both one-time payments and subscriptions. Some coupon object parameters, like `duration`, only apply to [subscriptions](/billing/subscriptions/coupons).

### Limit redemption usage

The `max_redemptions` and `redeem_by` values apply to the coupon across every application. For example, you can restrict a coupon to the first 50 usages of it, or you can make a coupon expire by a certain date.

### Limit eligible products

You can limit the products that are eligible for discounts using a coupon by adding the product IDs to the `applies_to` hash in the Coupon object. Any promotion codes that map to this coupon only apply to the list of eligible products.

### Delete a coupon

You can delete coupons in the Dashboard or the API. Deleting a coupon prevents it from being applied to future transactions or customers.

Create a promotion code
-----------------------

Promotion codes are customer-facing codes created on top of coupons. You can also specify additional restrictions that control when a customer can apply the promotion. You can share these codes with customers who can enter them during checkout to apply a discount.

To create a [promotion code](/api/promotion_codes), specify an existing `coupon` and any restrictions (for example, limiting it to a specific `customer`). If you have a specific code to give to your customer (for example, `FALL25OFF`), set the `code`. If you leave this field blank, we’ll generate a random `code` for you.

The `code` is case-insensitive and unique across active promotion codes for any customer. For example:

*   You can create multiple customer-restricted promotion codes with the same `code`, but you can’t reuse that `code` for a promotion code redeemable by any customer.
*   If you create a promotion code that is redeemable by any customer, you can’t create another active promotion code with the same `code`.
*   You can create a promotion code with `code: NEWUSER`, inactivate it by passing `active: false`, and then create a new promotion code with `code: NEWUSER`.

Promotion codes can be created in the coupons section of the [Dashboard](https://dashboard.stripe.com/coupons/create) or with the [API](/api#promotion_codes):

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/promotion_codes \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d coupon={{COUPON_ID}} \   -d code=VIPCODE`

Use a promotion code
--------------------

Enable customer-redeemable promotion codes using the [allow\_promotion\_codes](/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes) parameter in a Checkout Session. This enables a field in Checkout to allow customers to input promotion codes.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price_data][unit_amount]"=2000 \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][quantity]"=1 \  -d mode=payment \  -d allow_promotion_codes=true \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

Configure a promotion code
--------------------------

For each promotion code, you can customize eligible customers, redemptions, and other limits.

### Limit by customer

To limit a promotion to a particular customer, specify a [customer](/api/promotion_codes/create#create_promotion_code-customer) when creating the promotion code. If no customer is specified, any customer can redeem the code.

### Limit by first-time order

You can also limit the promotion code to first-time customers with [restrictions.first\_time\_transaction](/api/promotion_codes/create#create_promotion_code-restrictions-first_time_transaction). If the `customer` isn’t defined, or if a defined `customer` has no prior payments or non-void [invoices](/api/invoices "invoices"), it’s considered a first-time transaction.

#### Note

Sessions that don’t create [Customers](/api/customers) instead create [Guest Customers](https://support.stripe.com/questions/guest-customer-faq) in the Dashboard. Promotion codes limited to first-time customers are still accepted for these Sessions.

### Set a minimum amount

With promotion codes, you can set a minimum transaction amount for eligible discount by configuring [minimum\_amount](/api/promotion_codes/create#create_promotion_code-restrictions-minimum_amount) and [minimum\_amount\_currency](/api/promotion_codes/create#create_promotion_code-restrictions-minimum_amount_currency). Since promotion code restrictions are checked at redemption time, the minimum transaction amount only applies to the initial payment for a subscription.

### Customize expirations

You can set an expiration date on the promotion code using [expires\_at](/api/promotion_codes/create#create_promotion_code-expires_at). If the underlying coupon already has `redeem_by` set, then the expiration date for the promotion code can’t be later than that of the coupon. If `promotion_code[expires_at]` isn’t specified, the coupon’s `redeem_by` automatically populates `expires_at`.

For example, you might have plans to support a coupon for a year, but you only want it to be redeemable for one week after a customer receives it. You can set `coupon[redeem_by]` to one year from now, and set each `promotion_code[expires_at]` to one week after it’s created.

### Limit redemptions

You can limit the number of redemptions by using [max\_redemptions](/api/promotion_codes/create#create_promotion_code-max_redemptions), which works similarly to the coupon parameter. If the underlying coupon already has `max_redemptions` set, then the `max_redemptions` for the promotion code can’t be greater than that of the coupon.

For example, you might want a seasonal sale coupon to be redeemable by the first 50 customers, but the winter promotion can only use 20 of those redemptions. In this scenario, you can set `coupon[max_redemptions]: 50` and `promotion_code[max_redemptions]: 20`.

### Inactive promotions

You can set whether a promotion code is currently redeemable by using the [active](/api/promotion_codes/create#create_promotion_code-active) parameter. However, if the underlying coupon for a promotion code becomes invalid, all of its promotion codes become permanently inactive. Similarly, if a promotion code reaches its `max_redemptions` or `expires_at`, it becomes permanently inactive. You can’t reactivate these promotion codes.

### Delete promotions

You can delete promotions in the Dashboard or the API. Deleting a promotion prevents it from being applied to future transactions or customers.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Create a coupon](#create-a-coupon "Create a coupon")

[Use a coupon](#use-a-coupon "Use a coupon")

[Configure a coupon](#configure-a-coupon "Configure a coupon")

[Limit redemption usage](#limit-redemption-usage "Limit redemption usage")

[Limit eligible products](#limit-eligible-products "Limit eligible products")

[Delete a coupon](#delete-a-coupon "Delete a coupon")

[Create a promotion code](#create-a-promotion-code "Create a promotion code")

[Use a promotion code](#use-promotion-code "Use a promotion code")

[Configure a promotion code](#configure-a-promotion-code "Configure a promotion code")

[Limit by customer](#limit-by-customer "Limit by customer")

[Limit by first-time order](#limit-by-first-time-order "Limit by first-time order")

[Set a minimum amount](#set-a-minimum-amount "Set a minimum amount")

[Customize expirations](#customize-expirations "Customize expirations")

[Limit redemptions](#limit-redemptions "Limit redemptions")

[Inactive promotions](#inactive-promotions "Inactive promotions")

[Delete promotions](#delete-promotions "Delete promotions")

Products Used

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/manual-currency-prices

 Manual currency prices | Stripe Documentation     

[Skip to content](#main-content)

Define manual currency prices

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmanual-currency-prices)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmanual-currency-prices)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

Define manual currency prices

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

India

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Let customers pay in their local currency](/payments/checkout/adaptive-pricing "Let customers pay in their local currency")

Manual currency prices
======================

Present local currencies to customers with manual currency prices.
------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Stripe supports manually defining prices in different currencies when creating [products](/products-prices/overview#get-started). However, Stripe recommends leveraging [Adaptive Pricing](/payments/checkout/adaptive-pricing) instead of manual currency prices to reduce currency exchange rate fluctuation risk and to automatically enable support for 50+ local currencies.

Use manual currency prices over Adaptive Pricing when:

*   Adaptive Pricing isn’t yet [supported](/payments/checkout/adaptive-pricing#restrictions) for your business or Checkout configuration (reach out to [adaptive-pricing-beta@stripe.com](mailto:adaptive-pricing-beta@stripe.com) to inquire about the preview).
*   You’re supporting a region where you’re comfortable taking on fluctuations in the currency’s exchange rate.

Manually defined multi-currency prices override Adaptive Pricing for those currencies, even if it’s enabled.

[

Create a multi-currency price

Dashboard

Server-side




---------------------------------------------------------





](#add-multiple-currencies-to-a-price)

Dashboard

API

1.  Navigate to a product in the [Dashboard](https://dashboard.stripe.com/products?active=true).
2.  Click **+Add another price** to create a new price.
3.  Fill in the price and select a currency. This first currency is the price’s default currency. Make sure all of your prices have the same default currency.
4.  Click **+Add a price by currency** to search and select from supported currencies, adding them to your price.
5.  Use the multi-currency price you created by passing its ID into [line items](/api/checkout/sessions/create#create_checkout_session-line_items-price) when you create a Checkout Session.

[

Create a Checkout Session

Server-side




------------------------------------------





](#create-checkout-session)

Create a Checkout Session using the multi-currency price:

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_tR3PYbcVNZZ796tH88S4VQ2u  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

[

Testing

Server-side

Client-side




-------------------------------------





](#testing)

To test local currency presentment for Checkout, Payment Links, and the [pricing table](/payments/checkout/pricing-table), pass in a location-formatted customer email that includes a suffix in a `+location_XX` format in the local part of the email. `XX` must be a valid [two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm).

For example, to test currency presentment for a customer in France, pass in an email such as `test+location_FR@example.com`.

When you visit the URL for a Checkout Session, Payment Link, or pricing table created with a location-formatted email, you see the same currency as a customer does in the specified country.

### Testing Checkout

When you create a Checkout Session, pass the location-formatted email as [customer\_email](/api/checkout/sessions/object#checkout_session_object-customer_email) to simulate Checkout from a particular country.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u   sk_test_tR3PYbcVNZZ796tH88S4VQ2u  : \   -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \  -d success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode customer_email="test+location_FR@example.com"`

You can also create a [Customer](/api/customers/create) and specify their email that contains the `+location_XX` suffix. Stripe test cards work as usual.

When it’s possible to present the customer’s local currency in Checkout, the [Checkout Session](/api/checkout/sessions/object) object changes. Fields like `currency`, `payment_method_types`, and `amount_total` reflect the local currency and price.

### Testing Payment Links

For Payment Links, pass the location-formatted email as the `prefilled_email` [URL parameter](/payment-links/customize#customize-checkout-with-url-parameters) to test currency presentment for customers in different countries.

### Testing Pricing table

For the pricing table, pass the location-formatted email as the [customer-email](/payments/checkout/pricing-table#customer-email) attribute to test currency presentment for customers in different countries.

[

OptionalSpecify a currency

Server-side




-------------------------------------------





](#specify-currency)

Local payment methods
---------------------

The Checkout Session presents customers with popular payment methods compatible with their local currencies. For example, for customers located in the Netherlands, the Checkout Session converts prices to EUR and also present popular Dutch payment methods like iDEAL.

You can configure which payment methods you accept in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

Pricing tables
--------------

Manual currency prices also work with [pricing tables](/payments/checkout/pricing-table). To render local currencies to customers viewing your pricing table, all of the pricing table’s Prices must include the customer’s local currency in their `currency_options`. They must also include a `tax_behavior` for the given currency if you’re using Stripe Tax.

Supported integrations
----------------------

Checkout automatically presents the local currency to customers if all of the following are true:

*   The Checkout Session’s prices, shipping rates, and discounts have the relevant currency in their `currency_options`.
*   If a price on the Checkout Session has an upsell, the upsell’s price has the relevant currency in its `currency_options`.
*   For a Checkout Session using Stripe Tax, the `tax_behavior` on the Checkout Session is specified for the relevant currency for all of the Checkout Session’s prices, shipping rates, and discounts.
*   You didn’t specify a currency during Checkout Session creation.

If Checkout can’t localize the currency because the relevant currency option or `tax_behavior` is missing, the Session presents to the customer in the default currency. The default currency must be the same across all prices, shipping rates, and discounts.

### Restrictions

Price localization isn’t available for Checkout Sessions that:

*   Use manual tax rates.
*   Use `payment_intent_data.application_fee_amount` or `payment_intent_data.transfer_data.amount`.

Fees
----

Stripe’s standard transaction fees apply to automatically converted transactions:

*   Cards or payment methods fee
*   International cards or payment methods fee (if applicable)
*   Currency conversion fee

See the [pricing page](https://stripe.com/pricing) for more details about these fees.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Create a multi-currency price](#add-multiple-currencies-to-a-price "Create a multi-currency price")

[Create a Checkout Session](#create-checkout-session "Create a Checkout Session")

[Testing](#testing "Testing")

[Testing Checkout](#testing-checkout "Testing Checkout")

[Testing Payment Links](#testing-payment-links "Testing Payment Links")

[Testing Pricing table](#testing-pricing-table "Testing Pricing table")

[Local payment methods](#local-payment-methods "Local payment methods")

[Pricing tables](#pricing-table "Pricing tables")

[Supported integrations](#supported-integrations "Supported integrations")

[Restrictions](#restrictions "Restrictions")

[Fees](#fees "Fees")

Products Used

[

Checkout





](/payments/checkout)

[

Payment Links





](/payments/payment-links)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/customization/appearance

 Customize appearance | Documentación de Stripe     

[Ir a contenido](#main-content)

Personaliza el diseño

[

Crea una cuenta



](https://dashboard.stripe.com/register)o[

inicia sesión



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fappearance)

[

](/)

Busca en la documentación

/

[Crear cuenta](https://dashboard.stripe.com/register)

[

Iniciar sesión



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fappearance)

[

Empezar



](/get-started)

[

Pagos



](/payments)

[

Automatización de finanzas



](/finance-automation)

[

Plataformas y marketplaces



](/connect)

[

Banca como servicio



](/financial-services)

[

Herramientas para desarrolladores



](/development)

[

Empezar



](/get-started)

[

Pagos



](/payments)

[

Automatización de finanzas



](/finance-automation)

[

Empezar



](/get-started)

[

Pagos



](/payments)

[

Automatización de finanzas



](/finance-automation)

[

Plataformas y marketplaces



](/connect)

[

Banca como servicio



](/financial-services)

API y SDK

Ayuda

[Resumen](/payments)

Acerca de Stripe Payments

[Actualiza tu integración](/payments/upgrades "Mejora tu integración actual")

Análisis de pagos

Pagos por Internet

[Resumen](/payments/online-payments "Obtén información sobre las opciones de integración para aceptar pagos por Internet.")[Encuentra tu caso de uso](/payments/use-cases/get-started "Descubre cómo Stripe puede ayudar a tu empresa.")

Use Payment Links

Crear una página del proceso de compra

[Resumen](/payments/checkout/build-integration "Crea una experiencia de pagos con Checkout.")

[Guías de inicio rápido](/payments/checkout/quickstarts "Empieza con el código de muestra.")

[Personaliza el estilo](/payments/checkout/customization "Modifica la apariencia de tu página del proceso de compra. El nivel de personalización depende del producto que utilices.")

Personaliza el diseño

[Customize text and policies](/payments/checkout/customization/policies)

[Personaliza el comportamiento](/payments/checkout/customization/behavior)

[Utiliza tu dominio personalizado](/payments/checkout/custom-domains)

[Recolecta información adicional](/payments/checkout/collect-additional-info "Recolecta información como las direcciones de envío y los números de teléfono como parte del proceso de compra.")

[Cobrar impuestos](/payments/checkout/taxes)

[Actualiza forma dinámica el proceso de compra](/payments/checkout/dynamic-updates "Haz actualizaciones mientras tu cliente efectúa una compra.")

[Gestiona tu catálogo de productos](/payments/checkout/product-catalog)

[Suscripciones](/payments/subscriptions "Gestiona suscripciones con Checkout")

[Gestiona los métodos de pago](/payments/checkout/payment-methods)

[Permite que los clientes paguen en su divisa local](/payments/checkout/adaptive-pricing)

[Añade descuentos y ventas adicionales y cruzadas](/payments/checkout/promotions)

[Configurar pagos futuros](/payments/checkout/save-and-reuse "Descubre cómo guardar los datos de pago para cobrarles a tus clientes más tarde")

[Guardar datos de pago durante el pago](/payments/checkout/save-during-payment "Guardar datos de pago durante el pago")

[Después del pago](/payments/checkout/after-the-payment)

[Elements con el registro de cambios de la API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrar desde Checkout heredado](/payments/checkout/migration)

[Migrar Checkout para usar precios](/payments/checkout/migrating-prices)

Desarrolla una integración avanzada

Desarrolla una integración en la aplicación

Métodos de pago

Añadir métodos de pago

Gestiona los métodos de pago

Proceso de compra más rápido con Link

Interfaces de usuario de pagos

Payment Links

Checkout

Elements para la web

Elements en la aplicación

Escenarios de pago

Flujos de pagos personalizados

Capacidad adquirente flexible

Pagos en persona

Terminal

Otros productos de Stripe

Financial Connections

Criptomonedas

Climate

Enlaces de transferencia

Estados Unidos

Español (España)

[Inicio](/ "Inicio")[Pagos](/payments "Pagos")Build a checkout page[Customize look and feel](/payments/checkout/customization "Customize look and feel")

Customize appearance
====================

Customize your checkout page's colors, fonts, shapes, and more.
---------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Apply branding
--------------

You can apply custom branding to Checkout. Go to [Branding Settings](https://dashboard.stripe.com/settings/branding/checkout) to:

*   Upload a logo or icon
*   Customize the Checkout page’s background color, button color, font, and shapes

### Branding with Connect

For platforms performing direct charges, and destination charges with `on_behalf_of`, Checkout uses the brand settings of the connected account. For connected accounts without access to the full Stripe Dashboard (includes Express and Custom accounts), platforms can configure the brand settings with the [Accounts](/api/accounts/object#account_object-settings-branding) API.

Change your brand name
----------------------

You can change a Checkout page’s name by modifying the **Business name** field in [Business details settings](https://dashboard.stripe.com/settings/business-details).

You can also [customize the domain name](/payments/checkout/custom-domains) of a Stripe-hosted Checkout page.

Font compatibility
------------------

Each custom font is compatible with a [subset of locales](/js/appendix/supported_locales). You can either explicitly set the locale of a Checkout Session by passing the locale field when creating the Session, or use the default `auto` setting where Checkout chooses a locale based on the customer’s browser settings.

The following table lists unsupported locales for each font. Languages in these locales might fall outside of the supported character range for a given font. In those cases, Stripe renders the Checkout page with an appropriate system fallback font. If you choose a Serif font but it’s unsupported in a locale, Stripe falls back to a Serif-based font.

Font family

Unsupported locales

Be Vietnam Pro

`bg`, `el`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Bitter

`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Chakra Petch

`bg`, `el`, `ja`, `ko`, `ru`, `zh`, `zh-HK`, `zh-TW`

Hahmlet

`bg`, `el`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Inconsolata

`bg`, `el`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Inter

`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Lato

`bg`, `cs`, `el`, `hr`, `ja`, `ko`, `lt`, `lv`, `mt`, `ro`, `ru`, `sl`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`

Lora

`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

M PLUS 1 Code

`bg`, `el`, `ko`, `lt`, `lv`, `ru`, `sk`, `sl`, `th`, `tr`

Montserrat

`el`, `hr`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Nunito

`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Noto Sans

`ja`, `ko`, `th`

Noto Serif

`th`

Open Sans

`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

PT Sans

`el`, `ja`, `ko`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`

PT Serif

`el`, `ja`, `ko`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`

Pridi

`bg`, `el`, `ja`, `ko`, `ru`, `zh`, `zh-HK`, `zh-TW`

Raleway

`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Roboto

`ja`, `ko`, `zh`, `zh-HK`, `zh-TW`

Roboto Slab

`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Source Sans Pro

`bg`, `el`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Titillium Web

`bg`, `el`, `ja`, `ko`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`

Ubuntu Mono

`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Zen Maru Gothic

`bg`, `cs`, `el`, `hr`, `ko`, `lt`, `lv`, `pl`, `ro`, `ru`, `sk`, `th`, `vi`

¿Te ha sido útil la página?

SíNo

¿Necesitas ayuda? [Ponte en contacto con el equipo de soporte](https://support.stripe.com/).

Únete a nuestro [programa de acceso anticipado](https://insiders.stripe.dev/).

Consulta nuestro [registro de cambios de productos](https://stripe.com/blog/changelog).

¿Tienes alguna pregunta? [Ponte en contacto con el equipo de ventas](https://stripe.com/contact/sales).

Con tecnología de [Markdoc](https://markdoc.dev)

Inscríbete para recibir las actualizaciones para desarrolladores:

Inscríbete

Puedes cancelar la suscripción en cualquier momento. Consulta nuestra [Política de privacidad](https://stripe.com/privacy).

En esta página

[Apply branding](#branding "Apply branding")

[Branding with Connect](#branding-with-connect "Branding with Connect")

[Change your brand name](#change-your-brand-name "Change your brand name")

[Font compatibility](#font-compatibility "Font compatibility")

Productos utilizados

[

Checkout





](/payments/checkout)

[

Elements





](/payments/elements)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La experiencia con Stripe Shell es mejor en ordenadores de sobremesa.

    $

---

## URL: https://docs.stripe.com/payments/checkout/abandoned-carts

 放棄されたカートを回復する | Stripe のドキュメント      

[コンテンツにスキップ](#main-content)

放棄されたカートを回復する

[

アカウントを作成



](https://dashboard.stripe.com/register)または[

サインイン



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fabandoned-carts)

[

](/)

ドキュメントを検索

/

[アカウントを作成](https://dashboard.stripe.com/register)

[

サインイン



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fabandoned-carts)

[

始める



](/get-started)

[

支払い



](/payments)

[

財務の自動化



](/finance-automation)

[

プラットフォームおよびマーケットプレイス



](/connect)

[

サービスとしてのバンキング (BaaS)



](/financial-services)

[

開発者向けのツール



](/development)

[

始める



](/get-started)

[

支払い



](/payments)

[

財務の自動化



](/finance-automation)

[

始める



](/get-started)

[

支払い



](/payments)

[

財務の自動化



](/finance-automation)

[

プラットフォームおよびマーケットプレイス



](/connect)

[

サービスとしてのバンキング (BaaS)



](/financial-services)

API & SDK

ヘルプ

[概要](/payments)

Stripe Payments について

[構築済みのシステムをアップグレード](/payments/upgrades "既存の Stripe システムを改善")

支払いの分析

オンライン決済

[概要](/payments/online-payments "オンライン決済を受け付けるための実装オプションについてご紹介します。")[ユースケースを見つける](/payments/use-cases/get-started "Stripe が事業者をどのようにサポートするかをご紹介します。")

Use Payment Links

決済ページを構築

[概要](/payments/checkout/build-integration "Checkout を使用して決済体験を構築します。")

[クイックスタート](/payments/checkout/quickstarts "サンプルコードで開始できます。")

[デザインをカスタマイズする](/payments/checkout/customization "決済ページのデザインを管理します。カスタマイズのレベルはご利用のプロダクトによって異なります。")

[追加情報を収集する](/payments/checkout/collect-additional-info "決済プロセスの一環として配送先住所や電話番号などの情報を収集します。")

[税金を徴収する](/payments/checkout/taxes)

[決済フローを動的に更新](/payments/checkout/dynamic-updates "顧客が決済する際に更新します。")

[商品カタログを管理する](/payments/checkout/product-catalog)

[サブスクリプション](/payments/subscriptions "Checkout を使用してサブスクリプションを管理")

[決済手段を管理](/payments/checkout/payment-methods)

[顧客が現地通貨で支払いできるようにする](/payments/checkout/adaptive-pricing)

[割引、アップセル、クロスセルを追加](/payments/checkout/promotions)

[将来の支払いを設定する](/payments/checkout/save-and-reuse "支払いの詳細を保存し、後で顧客に請求する方法")

[支払い中に支払い詳細を保存する](/payments/checkout/save-during-payment "支払い中に支払い詳細を保存する")

[支払い後](/payments/checkout/after-the-payment)

[注文のフルフィルメント](/checkout/fulfillment)

[Send receipts and paid invoices](/payments/checkout/receipts)

[リダイレクトの動作をカスタマイズ](/payments/checkout/custom-success-page)

放棄されたカートを回復する

[コンバージョンファネルを分析](/payments/checkout/analyze-conversion-funnel)

[Checkout Sessions API を使用した Elements の変更ログ](/checkout/elements-with-checkout-sessions-api/changelog)

[従来の Checkout からの移行](/payments/checkout/migration)

[Checkout を移行して Prices を使用](/payments/checkout/migrating-prices)

高度なシステムを構築

アプリ内実装を構築

支払い方法

支払い方法を追加

決済手段を管理

Link による購入の迅速化

決済 UI

Payment Links

Checkout

Web Elements

アプリ内 Elements

決済シナリオ

カスタムの決済フロー

柔軟なアクワイアリング

店頭支払い

端末

他の Stripe プロダクト

Financial Connections

仮想通貨

Climate

Payout Links

日本

日本語

[ホーム](/ "ホーム")[支払い](/payments "支払い")Build a checkout page[After the payment](/payments/checkout/after-the-payment "After the payment")

#### 注

このページはまだ日本語ではご利用いただけません。より多くの言語で文書が閲覧できるように現在取り組んでいます。準備が整い次第、翻訳版を提供いたしますので、もう少しお待ちください。

放棄されたカートを回復する
=============

Checkout でのカート離脱を回復して、収益を向上させる方法をご紹介します。
----------------------------------------

Stripe がオンラインで提供するページ

オンラインフォーム

埋め込みコンポーネント

パブリックプレビュー版

E コマースでは、[カゴ落ち](/payments/checkout/compliant-promotional-emails)とは、顧客が購入の完了前に決済フローを離れる場合のことです。顧客を Checkout に戻すには、リカバリーフローを作成して、購入を完了するようメールで顧客に連絡をします。

カゴ落ちのメールは、広義では顧客に新製品について知らせたり、クーポンや割引を提供したりするための「プロモーションメール」カテゴリーに分類されます。顧客にメールを送信するには、顧客がプロモーションメールの受信に同意している必要があります。Checkout は以下に役立ちます。

1.  プロモーションメールを送信できるように顧客からの同意を収集します。
2.  顧客が Checkout を破棄したときに通知を受け取り、カートの破棄に関するメールを送信できるようにします。

[

プロモーションへの同意を収集する


------------------





](#collect-promotional-consent)

[プロモーション用コンテンツへの同意を収集](/payments/checkout/promotional-emails-consent)するように Checkout を設定します。顧客のメールアドレスを収集して、Checkout にリダイレクトされる前にプロモーション用コンテンツへの同意をリクエストする場合、`consent_collection[promotions]` をスキップできます。

Command Line

言語を選択cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_09l3shTSTKHYCzzZZsiLl2vA  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d customer=  {{CUSTOMER_ID}}   \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \  -d "consent_collection[promotions]"=auto`

[

リカバリーを設定する


------------





](#configure-recovery)

Checkout セッションは、その [expires\_at](/api/checkout/sessions/object#checkout_session_object-expires_at) タイムスタンプに達すると、顧客が購入していなくても破棄されます。この場合、セッションにアクセスできなくなり、Stripe が `checkout.session.expired` [Webhook](/webhooks "Webhook") を起動します。この Webhook をリッスンすることで、顧客を新しい Checkout セッションに戻して購入を完了してもらう機会を作ることができます。この機能を使用するには、セッションの作成時に `after_expiration.recovery` を有効にします。

Command Line

言語を選択cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_09l3shTSTKHYCzzZZsiLl2vA  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \  -d customer=  {{CUSTOMER_ID}}   \  -d "consent_collection[promotions]"=auto \  -d "after_expiration[recovery][enabled]"=true \  -d "after_expiration[recovery][allow_promotion_codes]"=true`

[

カート放棄についての通知を受ける


------------------





](#webhook)

Listen to the `checkout.session.expired` webhook to be notified when customers abandon Checkout and sessions expire. When the session expires with recovery enabled, the webhook payload contains [after\_expiration](/api/checkout/sessions/object#checkout_session_object-after_expiration-recovery), which includes a URL denoted by `after_expiration.recovery.url` that you can embed in cart abandonment emails. When the customer opens this URL, **it creates a new Checkout Session that’s a copy of the original expired session**. The customer uses this copied session to complete the purchase.

#### 注

For security purposes, the recovery URL for a session is usable for 30 days, denoted by the `after_expiration.recovery.expires_at` timestamp.

`{   "id": "evt_123456789",   "object": "event",   "type": "checkout.session.expired",   // ...other webhook attributes   "data": {     "object": {       "id": "cs_12356789",       "object": "checkout.session",       // ...other Checkout Session attributes       "consent_collection": {         "promotions": "auto",       },       "consent": {         "promotions": "opt_in"       },       "after_expiration": {         "recovery": {           "enabled": true,           "url": "[https://buy.stripe.com/r/live_asAb1724](https://buy.stripe.com/r/live_asAb1724)",           "allow_promotion_code": true,           "expires_at": 1622908282,         }       }     }   } }`

[

リカバリーメールを送信する


---------------





](#send-recovery-emails)

To send recovery emails, create a webhook handler for expired sessions and send an email that embeds the session’s recovery URL. A customer might abandon multiple Checkout Sessions, each triggering its own `checkout.session.expired` event so make sure to record when you send recovery emails to customers and avoid spamming them.

言語を選択Node

``// Find your endpoint's secret in your Dashboard's webhook settings const endpointSecret = 'whsec_...';  // Using Express const app = require('express')();  // Use body-parser to retrieve the raw body as a buffer const bodyParser = require('body-parser');  const sendRecoveryEmail = (email, recoveryUrl) => {   // TODO: fill me in   console.log("Sending recovery email", email, recoveryUrl); }  app.post('/webhook', bodyParser.raw({type: 'application/json'}), (request, response) => {   const payload = request.body;   const sig = request.headers['stripe-signature'];    let event;    try {     event = stripe.webhooks.constructEvent(payload, sig, endpointSecret);   } catch (err) {     return response.status(400).send(`Webhook Error: ${err.message}`);   }    // Handle the checkout.session.expired event   if (event.type === 'checkout.session.expired') {     const session = event.data.object;      // When a Checkout Session expires, the customer's email isn't returned in     // the webhook payload unless they give consent for promotional content     const email = session.customer_details?.email     const recoveryUrl = session.after_expiration?.recovery?.url      // Do nothing if the Checkout Session has no email or recovery URL     if (!email || !recoveryUrl) {       return response.status(200).end();     }      // Check if the customer has consented to promotional emails and     // avoid spamming people who abandon Checkout multiple times     if (       session.consent?.promotions === 'opt_in'       && !hasSentRecoveryEmailToCustomer(email)     ) {       sendRecoveryEmail(email, recoveryUrl)     }   }   response.status(200).end(); });``

[

オプションセッションの有効期限を調整する


----------------------





](#adjust-session-expiration)

[

オプションコンバージョン率を追跡する


--------------------





](#track-conversion)

[

オプションリカバリーメールでプロモーションコードを提供する


-------------------------------





](#promotion-codes)

このページはお役に立ちましたか。

はいいいえ

お困りのことがございましたら 、[サポートにお問い合わせください](https://support.stripe.com/)。

[早期アクセスプログラム](https://insiders.stripe.dev/)にご参加ください。

Stripe の[製品変更ログ](https://stripe.com/blog/changelog)を確認してください。

ご不明な点がございましたら、[お問い合わせください](https://stripe.com/contact/sales)。

Powered by [Markdoc](https://markdoc.dev)

開発者向けの最新情報に登録:

登録

登録はいつでも解除できます。Stripe の[プライバシーポリシー](https://stripe.com/privacy)をお読みください。

このページの内容

[プロモーションへの同意を収集する](#collect-promotional-consent "プロモーションへの同意を収集する")

[リカバリーを設定する](#configure-recovery "リカバリーを設定する")

[カート放棄についての通知を受ける](#webhook "カート放棄についての通知を受ける")

[リカバリーメールを送信する](#send-recovery-emails "リカバリーメールを送信する")

使用製品

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

Stripe Shell にはデスクトップが最適です。

    $

---

## URL: https://docs.stripe.com/payments/checkout/collect-additional-info

 Collecte d'informations supplémentaires | Documentation Stripe     

[Accéder directement au contenu](#main-content)

Collecter des informations supplémentaires

[

Créez un compte



](https://dashboard.stripe.com/register)ou[

connecter-vous



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcollect-additional-info)

[

](/)

Rechercher dans la documentation

/

[Créez un compte](https://dashboard.stripe.com/register)

[

Connectez-vous



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcollect-additional-info)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Plateformes et places de marché



](/connect)

[

Services bancaires



](/financial-services)

[

Outils de développement



](/development)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Démarrer



](/get-started)

[

Paiements



](/payments)

[

Automatisation des opérations financières



](/finance-automation)

[

Plateformes et places de marché



](/connect)

[

Services bancaires



](/financial-services)

API et SDK

Aide

[Aperçu](/payments)

À propos des paiements Stripe

[Mettre votre intégration à niveau](/payments/upgrades "Améliorer votre intégration existante")

Analyses des paiements

Paiements en ligne

[Présentation](/payments/online-payments "Découvrez les possibilités d'intégration pour accepter des paiements en ligne.")[Trouver votre cas d'usage](/payments/use-cases/get-started "Découvrez comment Stripe peut accompagner votre entreprise.")

Use Payment Links

Créer une page de paiement

[Présentation](/payments/checkout/build-integration "Créez une expérience de paiement avec Checkout.")

[Solutions de démarrage rapide](/payments/checkout/quickstarts "Démarrez avec des exemples de code.")

[Personnaliser l'apparence](/payments/checkout/customization "Contrôlez l'apparence de la page de paiement. Le degré de personnalisation dépend du produit que vous utilisez.")

Collecter des informations supplémentaires

[Collecter les adresses physiques](/payments/collect-addresses "Découvrez comment recueillir les adresses de facturation et de livraison.")

[Facturer la livraison](/payments/during-payment/charge-shipping)

[Collecter des numéros de téléphone](/payments/checkout/phone-numbers "Collecter le numéro de téléphone des clients avec Checkout")

[Ajouter des champs personnalisés](/payments/checkout/custom-fields)

[Recueillir le consentement pour les e-mails promotionnels](/payments/checkout/promotional-emails-consent)

[Collecter des taxes](/payments/checkout/taxes)

[Mise à jour dynamique lors du paiement](/payments/checkout/dynamic-updates "Effectuez des mises à jour pendant que votre client procède au paiement.")

[Gérer votre catalogue de produits](/payments/checkout/product-catalog)

[Abonnements](/payments/subscriptions "Gérer des abonnements avec Checkout")

[Gérer les moyens de paiement](/payments/checkout/payment-methods)

[Offrir aux clients la possibilité de payer dans leur devise locale](/payments/checkout/adaptive-pricing)

[Ajouter des réductions, des ventes incitatives et des ventes croisées](/payments/checkout/promotions)

[Configurer des paiements futurs](/payments/checkout/save-and-reuse "Comment enregistrer les données de paiement de vos clients et les débiter ultérieurement")

[Enregistrer les coordonnées bancaires lors du paiement](/payments/checkout/save-during-payment "Enregistrer les coordonnées bancaires lors du paiement")

[Après le paiement](/payments/checkout/after-the-payment)

[Liste des modifications de Elements avec l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrer depuis l'ancienne version de Checkout](/payments/checkout/migration)

[Migrer vers Checkout pour utiliser Prices](/payments/checkout/migrating-prices)

Développer une intégration avancée

Développer une intégration dans l'application

Moyens de paiement

Ajouter des moyens de paiement

Gérer les moyens de paiement

Paiement accéléré avec Link

Interfaces de paiement

Payment Links

Checkout

Web Elements

Elements intégrés à l'application

Scénarios de paiement

Tunnels de paiement personnalisés

Acquisition flexible

Paiements par TPE

Terminal

Autres produits Stripe

Financial Connections

Cryptomonnaies

Climate

Payout Links

France

Français (France)

[Accueil](/ "Accueil")[Paiements](/payments "Paiements")Build a checkout page

Collecte d'informations supplémentaires
=======================================

Collectez les informations relatives à la livraison et d'autres données du client au moment du paiement.
--------------------------------------------------------------------------------------------------------

[

Collecter les adresses physiques

Collectez les adresses et les numéros de téléphone lors du processus de paiement.

](/payments/collect-addresses "Collecter les adresses physiques")

[

Facturer la livraison

Créez des frais de livraison différents pour vos clients.

](/payments/during-payment/charge-shipping "Facturer la livraison")

[

Collecter des numéros de téléphone

Collectez les numéros de téléphone de vos clients avec l’API Checkout.

](/payments/checkout/phone-numbers "Collecter des numéros de téléphone")

[

Ajouter des champs personnalisés

Ajoutez des champs personnalisés à votre formulaire de paiement.

](/payments/checkout/custom-fields "Ajouter des champs personnalisés")

[

Recueillir le consentement à l'envoi d'e-mails promotionnels

Recueillez le consentement de vos clients à l’envoi d’e-mails promotionnels.

](/payments/checkout/promotional-emails-consent "Recueillir le consentement à l'envoi d'e-mails promotionnels")

[

Conformité des e-mails promotionnels

Découvrez comment vous assurer que vos e-mails promotionnels sont conformes.

](/payments/checkout/compliant-promotional-emails "Conformité des e-mails promotionnels")

Cette page vous a-t-elle été utile ?

OuiNon

Besoin d'aide ? [Contactez le service Support](https://support.stripe.com/).

Rejoignez notre [programme d'accès anticipé](https://insiders.stripe.dev/).

Consultez notre [journal des modifications des produits](https://stripe.com/blog/changelog).

Des questions ? [Contactez l'équipe commerciale](https://stripe.com/contact/sales).

Propulsé par [Markdoc](https://markdoc.dev)

Inscrivez-vous pour recevoir les mises à jour destinées aux développeurs :

S'inscrire

Vous pouvez vous désabonner à tout moment. Lisez notre [politique de confidentialité](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

Le shell Stripe est plus optimisé sur la version bureau.

    $

---

## URL: https://docs.stripe.com/payments/checkout/pay-what-you-want

 Let customers decide what to pay | Documentazione Stripe     

[Passa al contenuto](#main-content)

Consenti ai clienti di decidere cosa pagare

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpay-what-you-want)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpay-what-you-want)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Gestire un inventario limitato](/payments/checkout/managing-limited-inventory)

[Rendere modificabili le quantità delle voci riga](/payments/checkout/adjustable-quantity)

Consenti ai clienti di decidere cosa pagare

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page[Manage your product catalog](/payments/checkout/product-catalog "Manage your product catalog")

Let customers decide what to pay
================================

Accept tips and donations, or sell pay-what-you-want products and services.
---------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

### Inline pricing

If you maintain your product catalog outside of Stripe, you might want to use [inline pricing](/products-prices/pricing-models#inline-pricing). With inline pricing, you set inline prices for products or services when you create a Checkout Session.

You can also use inline pricing to collect donations. However, unlike pay-what-you-want pricing, you can’t reuse or update inline prices, and they’re only available through the API.

You can use this feature to collect a tip for a service provided, accept donations for a cause, or give your customers the option to pay what they want for your product or service. Go to Stripe Support to learn more about Stripe’s [requirements for accepting tips or donations](https://support.stripe.com/questions/requirements-for-accepting-tips-or-donations).

Pay-what-you-want payments have the following limitations:

*   You can’t add any other line items and the quantity can only be 1.
*   You can’t use promotion codes or discounts with them.
*   They don’t support recurring payments or cross-sells.

![Custom amounts](https://b.stripecdn.com/docs-statics-srv/assets/custom-amount.4e76797d1a181222160b2754643e4ee1.png)

[

Set up your product catalog


-----------------------------





](#product-catalog)

Stripe Checkout uses [Products](/api/products "Prodotti") and [Prices](/api/prices "Prezzi") to structure pay-what-you-want payments. In the following example, Togethere is selling tickets to a fundraising dinner and wants to allow their customers to pay what they want for their tickets.

Dashboard

API

To create a pay-what-you-want model on Stripe through the Dashboard, complete these steps:

1.  Create the `Fundraising dinner` product.
    
    1.  Go to **More** > **Product catalog**.
    2.  Click **+Add product**.
    3.  Enter the **Name** of the product (`Fundraising dinner`).
    4.  _(Optional)_ Add a **Description**. The customer sees the description at checkout.
2.  Create the price for the `Fundraising dinner` product:
    
    1.  Click on **More pricing options** at the bottom.
    2.  Select **One-off**.
    3.  Select **Customer chooses price** in the **Choose your pricing model** dropdown.
    4.  _(Optional)_ Add a suggested price.
    5.  _(Optional)_ Specify limits that the customer can input.
    6.  Click **Next** and **Add product**.

[

Create a Checkout Session


---------------------------





](#create-checkout-session)

To enable customers to change the amount on the payment page, use the price ID when you create a Checkout Session. If you select **Customer chooses price** as your pricing model, you can’t add any other line items and the quantity can only be 1.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \   --data-urlencode cancel_url="[https://example.com](https://example.com)" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Set up your product catalog](#product-catalog "Set up your product catalog")

[Create a Checkout Session](#create-checkout-session "Create a Checkout Session")

Prodotti utilizzati

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/pricing-table

 Embeddable pricing table for SaaS businesses | Stripe Documentation     

[Skip to content](#main-content)

Embed a pricing table

[

Create account



](https://dashboard.stripe.com/register/billing)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpricing-table)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register/billing)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpricing-table)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/finance-automation)

Billing

[Overview](/billing)

[About the Billing APIs](/billing/billing-apis)

[Subscriptions](/subscriptions)

[Overview](/billing/subscriptions/overview "Learn about the lifecycles of Stripe Billing’s subscriptions and invoices")

[Quickstart](/billing/quickstart "Quickstart")

[Use cases](/billing/subscriptions/use-cases)

[Build your integration](/billing/subscriptions/integration)

[Subscription features](/billing/subscriptions/features)

[Subscription invoices](/billing/invoices/subscription "Learn how to manage subscription invoices")

[Subscription schedules](/billing/subscriptions/subscription-schedules "Learn about subscription schedules and how to use them")

Subscription pricing

[Recurring pricing models](/products-prices/pricing-models "Understand and build models for recurring prices")

Embed a pricing table

Start subscriptions

[Set quantities](/billing/subscriptions/quantities "Vary the cost of a subscription by subscribing a customer to multiple quantities of a product")

[Set billing cycles](/billing/subscriptions/billing-cycle "Learn how to set the billing date for subscriptions")

[Backdate subscriptions](/billing/subscriptions/backdating "Bill customers for time that has already elapsed.")

[Subscribe to multiple items](/billing/subscriptions/multiple-products "Create subscriptions with multiple products, all billed in a single invoice.")

[Set trial periods](/billing/subscriptions/trials "Delay payments on active subscriptions using trial periods.")

[Apply coupons](/billing/subscriptions/coupons "Add discounts to a subscription using coupons and promotion codes")

[Migrate subscriptions to Stripe](/billing/subscriptions/migrate-subscriptions "Import subscriptions from other sources into Stripe")

Subscription payments

[Subscription payment methods](/billing/subscriptions/payment-methods-setting "Learn how to specify which payment methods are allowed for a subscription.")

[Integrate with third-party payment processing](/billing/subscriptions/third-party-payment-processing "Use Stripe subscriptions and invoices with third-party payment processors")

[Collection methods](/billing/collection-method "Configure your preferred method to collect on invoices and subscriptions")

[Share a link to update payment details](/billing/subscriptions/update-payment-method "Give your customers links they can use to update subscription payment details")

[Strong Customer Authentication (SCA)](/billing/migration/strong-customer-authentication "Update your integration to support Strong Customer Authentication (SCA) requirements")

Manage subscriptions

[Modify subscriptions](/billing/subscriptions/change "Learn how to change existing subscriptions.")

[Manage pending updates](/billing/subscriptions/pending-updates "Learn how to handle payment failures when updating a subscription")

[Analytics](/billing/subscriptions/analytics "Use the Dashboard to view metrics about your subscriptions.")

[Invoicing](/invoicing "Create and manage invoices for one-off payments")

[Usage-based Billing](/billing/subscriptions/usage-based)

[Connect and Billing](/billing/multi-entity-business)

[Tax and Billing](/billing/taxes)

[Quotes](/quotes "Learn about quotes")

[Revenue recovery](/billing/revenue-recovery "Learn about automated revenue recovery features for subscriptions")

[Automations](/billing/automations)

[Revenue recognition](/revenue-recognition/methodology/subscriptions-and-invoicing "Use Revenue Recognition with subscriptions")

[Customer management](/customer-management "Learn how to enable self-serve customer management")

[Entitlements](/billing/entitlements "Determine when you can grant your customers access to your product's features and when to revoke access.")

[Test your integration](/billing/testing "Test your billing integration")

Tax

Reporting

Data

Startup incorporation

Sweden

English (United Kingdom)

[Home](/ "Home")[Finance automation](/finance-automation "Finance automation")Billing[Subscriptions](/subscriptions "Subscriptions")[Subscription features](/billing/subscriptions/features "Subscription features")

Embeddable pricing table for SaaS businesses
============================================

Display a pricing table on your website and take customers directly to Stripe Checkout.
---------------------------------------------------------------------------------------

You can use the Stripe Dashboard to create a table that displays different subscription pricing levels to your customers. You don’t need to write any custom code to create or embed a pricing table. This guide describes how to:

*   Use the Stripe Dashboard to configure the UI component
*   Copy the generated code from the Dashboard
*   Embed the code on your website to show your customers pricing information and take them to a checkout page

Overview
--------

![The pricing table is an embedded UI that displays pricing information and takes customers to checkout.](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-embed.b27a06fcd84b57a8866a8b4b62323fdc.png)

Embed a pricing table on your website to display pricing details and convert customers to checkout.

A pricing table is an embeddable UI that:

*   Displays [pricing information](/products-prices/pricing-models "pricing model") and takes customers to a prebuilt checkout flow. The checkout flow uses [Stripe Checkout](/payments/checkout) to complete the purchase.
*   Supports common subscription business models like [flat-rate](/products-prices/pricing-models#flat-rate), [per-seat](/products-prices/pricing-models#per-seat), [tiered pricing](/products-prices/pricing-models#tiered-pricing), and free trials.
*   Lets you configure, customize, and update product and pricing information directly in the Dashboard, without needing to write any code.
*   Embeds into your website with a `<script>` tag and web component. Stripe automatically generates the tag. You copy and paste it into your website’s code.

The diagram below summarizes how the customer goes from viewing a pricing table to completing checkout.

Customer

Your application

Stripe Checkout

Views pricing table

Clicks on “subscribe” button

Completes purchase

Returns to your website

checkout.session.completed

Pricing table

[

Create pricing table


----------------------





](#Create)

1.  In the Dashboard, go to **More** > **Product catalog** > [pricing tables](https://dashboard.stripe.com/pricing-tables).
2.  Click **+Create pricing table**.
3.  Add products relevant to your customers (up to four per pricing interval). Optionally, include a free trial.
4.  Adjust the look and feel in **Display settings**. Highlight a specific product and customize the language, colors, font, and button design, then click **Continue**.
5.  Configure **Payment settings** to select the customer information to collect, options to present to the customer, and whether to display a confirmation page or redirect customers back to your site after a successful purchase.
    
    #### Confirm maximum quantity
    
    If you have tiered pricing that supports quantities greater than the default maximum of 99, check the **Let customers adjust quantity** property and increase the **Max** value accordingly. Tiered pricing options for quantities above the maximum don’t appear in the selector.
    
6.  Configure the [customer portal](/no-code/customer-portal) by clicking **Continue**.
7.  Click **Copy code** to copy the generated code and [embed it into your website](/no-code/pricing-table#embed).

![Customizing a pricing table](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-1.45ac9351d8f043a0a63554b89b2cedfc.png)

Customize your pricing table

![Configure payment settings](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-2.07d5287026b797b9aa1905c6ad99958d.png)

Configure payment settings

[

Embed pricing table


---------------------





](#embed)

After creating a pricing table, Stripe automatically returns an embed code composed of a `<script>` tag and a `<stripe-pricing-table>` web component. Click the **Copy code** button to copy the code and paste it into your website.

![Pricing table detail page](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-detail-page.dee9a93d69e802759dabd0e4ce62f1bd.png)

Copy the pricing table’s code and embed it on your website.

If you’re using HTML, paste the embed code into the HTML. If you’re using React, include the `script` tag in your `index.html` page to mount the `<stripe-pricing-table>` component.

#### Caution

The pricing table uses your account’s [publishable API key](/keys). If you revoke the API key, you need to update the embed code with your new publishable API key.

pricing-page.html

HTML

`<body>   <h1>We offer plans that help any business!</h1>   <!-- Paste your embed code script here. -->   <script     async     src="[https://js.stripe.com/v3/pricing-table.js](https://js.stripe.com/v3/pricing-table.js)">   </script>   <stripe-pricing-table     pricing-table-id=  '{{PRICING_TABLE_ID}}'      publishable-key=  "pk_test_4QHSdRjQiwkzokPPCiK33eOq"    >   </stripe-pricing-table> </body>`

[

Track subscriptions


---------------------





](#track-subscriptions)

When a customer purchases a subscription, you’ll see it on the [subscriptions page](https://dashboard.stripe.com/subscriptions) in the Dashboard.

### Handle fulfillment with the Stripe API

The pricing table component uses Stripe Checkout to render a prebuilt, hosted payment page. When a payment is completed using Checkout, Stripe sends the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event. Register an [event destination](/event-destinations) to receive the event at your endpoint to process fulfillment and reconciliation. See the [Checkout fulfillment guide](/checkout/fulfillment) for more details.

The `<stripe-pricing-table>` web component supports setting the `client-reference-id` property. When the property is set, the pricing table passes it to the Checkout Session’s [client\_reference\_id](/api/checkout/sessions/object#checkout_session_object-client_reference_id) attribute to help you reconcile the Checkout Session with your internal system. This can be an authenticated user ID or a similar string. `client-reference-id` can be composed of alphanumeric characters, dashes, or underscores, and be any value up to 200 characters. Invalid values are silently dropped and your pricing table will continue to work as expected.

#### Caution

Since the pricing table is embedded on your website and is accessible to anyone, check that `client-reference-id` does not include sensitive information or secrets, such as passwords or API keys.

pricing-page.html

HTML

`<body>   <h1>We offer plans that help any business!</h1>   <!-- Paste your embed code script here. -->   <script     async     src="[https://js.stripe.com/v3/pricing-table.js](https://js.stripe.com/v3/pricing-table.js)">   </script>   <stripe-pricing-table     pricing-table-id=  '{{PRICING_TABLE_ID}}'      publishable-key=  "pk_test_4QHSdRjQiwkzokPPCiK33eOq"      client-reference-id="{{CLIENT_REFERENCE_ID}}"   >   </stripe-pricing-table> </body>`

[

OptionalAdd product marketing features


----------------------------------------





](#product-marketing-features)

[

OptionalAdd a custom call-to-action


-------------------------------------





](#custom-cta)

[

OptionalPass the customer email


---------------------------------





](#customer-email)

[

OptionalPass an existing customer


-----------------------------------





](#customer-session)

[

OptionalCustomize the post-purchase experience


------------------------------------------------





](#post-purchase-experience)

[

OptionalUpdate pricing table


------------------------------





](#update)

[

OptionalConfigure free trials


-------------------------------





](#free-trials)

[

OptionalContent Security Policy


---------------------------------





](#csp)

[

OptionalLet customers manage their subscriptions

No code




-------------------------------------------------------------





](#customer-portal)

[

OptionalPresent local currencies


----------------------------------





](#price-localization)

[

OptionalAdd custom fields


---------------------------





](#custom-fields)

Limitations
-----------

*   **Business models**—The pricing table supports common subscription business models like flat-rate, per-seat, tiered pricing, and trials. Other [advanced pricing models](/billing/subscriptions/usage-based/pricing-models) aren’t supported.
*   **Product and price limits**—You can configure the pricing table to display a maximum of four products, with up to three prices per product. You can only configure three unique pricing intervals across all products.
*   **Account creation**—The pricing table call-to-action takes customers directly to checkout. It doesn’t currently support adding an intermediate step (for example, asking the customer to create an account on your website before checking out).
*   **Rate limit**—The pricing table has a [rate limit](/rate-limits) of up to 50 read operations per second. If you have multiple pricing tables, the rate limit is shared.
*   **Checkout redirect**—The pricing table can’t redirect customers to checkout if your website provider sandboxes the embed code in an iframe without the `allow-top-navigation` attribute enabled. Contact your website provider to enable this setting.
*   **Testing the pricing table locally**—The pricing table requires a website domain to render. To test the pricing table locally, run a local HTTP server to host your website’s `index.html` file over the `localhost` domain. To run a local HTTP server, use Python’s [SimpleHTTPServer](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server#running_a_simple_local_http_server) or the [http-server](https://www.npmjs.com/package/http-server) npm module.
*   **Connect**—The pricing table isn’t designed to work with [Connect](/connect "Connect") and doesn’t support features like a platform collecting fees.

Limit customers to one subscription
-----------------------------------

You can redirect customers that already have a subscription to the [customer portal](/billing/subscriptions/customer-portal "customer portal") or your website to manage their subscription. Learn more about [limiting customers to one subscription](/payments/checkout/limit-subscriptions).

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access programme](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Overview](#overview "Overview")

[Create pricing table](#Create "Create pricing table")

[Embed pricing table](#embed "Embed pricing table")

[Track subscriptions](#track-subscriptions "Track subscriptions")

[Handle fulfillment with the Stripe API](#handle-fulfillment-with-the-stripe-api "Handle fulfillment with the Stripe API")

[Limitations](#limitations "Limitations")

[Limit customers to one subscription](#limit-subscriptions "Limit customers to one subscription")

Products Used

[

Billing





](/billing)

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/how-checkout-works?oo-step=true&should-crawl=true&record-id=xkc4l55xdi&wait-before-scraping=2000&save-html=true&save-markdown=true

 How Checkout works | Stripe Documentation     

[Skip to content](#main-content)

How Checkout works

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

[Overview](/payments/checkout)

How Checkout works

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Checkout

How Checkout works
==================

Learn how to use Checkout to collect payments on your website.
--------------------------------------------------------------

Checkout is a low-code payment integration that creates a customizable form for collecting payments.

Checkout’s built-in features allow you to reduce your development time. It supports 40+ payment methods, including [Link](/payments/link), which lets your customers save their payment method for faster checkout. You can accept payments by embedding Checkout directly into your website, redirecting customers to a Stripe-hosted payment page, or creating a customized checkout page with [Stripe Elements](/payments/elements). Checkout supports payments for both [one-time purchases](/payments/online-payments) and [subscriptions](/subscriptions).

You can also customize Checkout and access additional functionality with the [Checkout Sessions API](/api/checkout/sessions) and the Stripe Dashboard. For a complete list of features, see its [built-in and customizable features](/payments/checkout/how-checkout-works#features).

Stripe-hosted page

Embedded form

Embedded components

Public preview

Checkout lifecycle
------------------

1.  When customers are ready to complete their purchase, your application creates a new Checkout Session.
2.  The Checkout Session provides a URL that redirects customers to a Stripe-hosted payment page.
3.  Customers enter their payment details on the payment page and complete the transaction.
4.  After the transaction, a [webhook](/webhooks "webhook") [fulfills the order](/checkout/fulfillment) using the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event.

Client

Server

Stripe API

Stripe Checkout

Send order information

Create Checkout Session

Return Checkout Session

checkout.session.created

Redirect customer to `url` from Checkout Session

Customer completes payment

Customer returns to your application

Handle fulfillment

checkout.session.completed

A diagram of a Stripe-hosted page integration's lifecycle

Low-code integration
--------------------

Checkout requires minimal coding and is the best choice for most integrations because of its prebuilt functionalities and customization options. You can integrate Checkout by creating a Checkout Session and collecting customer payment details. Collect payments by redirecting customers to a [Stripe-hosted payment page](/payments/accept-a-payment?platform=web&ui=stripe-hosted).

[Compare Checkout](/payments/online-payments#compare-features-and-availability) to other Stripe payment options to determine the best one for you. Checkout displays a payment form to collect customer payment information, validates cards, handles errors, and so on.

Built-in and customizable features
----------------------------------

Stripe Checkout has the following built-in and customizable features:

### Built-in features

*   Support for digital wallets and Link
*   Responsive mobile design
*   SCA-ready
*   CAPTCHAs
*   PCI compliance
*   Card validation
*   Error messaging
*   [Adjustable quantities](/payments/checkout/adjustable-quantity)
*   [Automatic tax collection](/tax/checkout)
*   International language support
*   [Adaptive Pricing](/payments/checkout/adaptive-pricing)

### Customizable features

*   [Collect taxes](/payments/checkout/taxes)
*   [Custom branding with colors, buttons, and font](/payments/checkout/customization)
*   [Cross-sells](/payments/checkout/cross-sells)
*   [Global payment methods](/payments/dashboard-payment-methods)
*   [Subscription upsells](/payments/checkout/upsells)
*   [Custom domains](/payments/checkout/custom-domains) (Stripe-hosted page only)
*   [Email receipts](/receipts)
*   [Apply discounts](/payments/checkout/discounts)
*   [Custom success page](/payments/checkout/custom-success-page)
*   [Recover abandoned carts](/payments/checkout/abandoned-carts)
*   [Autofill payment details with Link](/payments/checkout/customization/behavior#link)
*   [Collect Tax IDs](/tax/checkout/tax-ids)
*   [Collect shipping information](/payments/collect-addresses?payment-ui=checkout)
*   [Collect phone numbers](/payments/checkout/phone-numbers)
*   [Set the subscription billing cycle date](/payments/checkout/billing-cycle)

### Custom branding

You can set fonts, colors, icons, and field styles for your Stripe-hosted Checkout page using the [Branding settings](https://dashboard.stripe.com/settings/branding/checkout) in the Dashboard. For more information, see [Customize your integration](/payments/checkout/customization).

### Custom domains

If you use Stripe’s [custom domain feature](/payments/checkout/custom-domains), you can serve Stripe-hosted Checkout pages on a subdomain of your custom domain. Custom domains are a paid feature. For information, see [Pricing and fees](https://stripe.com/pricing).

Checkout Session
----------------

The Checkout Session is a programmatic representation of what your customers see on the checkout page. After creating a Checkout Session, redirect your customers to the Session’s URL to complete the purchase. When customers complete their purchase, you can [fulfill their orders](/checkout/fulfillment) by configuring an [event destination](/event-destinations) to process Checkout Session events. This code snippet from the [quickstart guide](/checkout/quickstart) is an example of how to create a Checkout Session in your application.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

### One-time and recurring payments

Allow customers to make one-time payments or subscribe to a product or service by setting the [mode](/api/checkout/sessions/create#create_checkout_session-mode) parameter in a Checkout Session.

Mode

Purchase type

Payment

One-time purchases

[Subscription](/billing/subscriptions/overview)

*   Recurring purchases
*   Mixed cart: Recurring purchases with one-time purchases

### Mixed cart

Create a mixed cart in Checkout that lets your customers purchase Subscription items and one-time purchase items at the same time. To create a mixed cart, set the `mode` parameter to `subscription` and include the Price IDs, or `price_data`, for each line\_item in the [line\_items](/api/checkout/sessions/create#create_checkout_session-line_items) array. Price IDs come from Price objects created using the Stripe Dashboard or API and allow you to store information about your product catalog in Stripe.

You can also use [price\_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data) to reference information from an external database where you’re hosting price and product details without storing product catalog information on Stripe. For more information, see [Build a subscriptions integration](/billing/subscriptions/build-subscriptions).

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"={{RECURRING_PRICE_ID}} \   -d "line_items[0][quantity]"=1 \  -d "line_items[1][price]"={{ONE_TIME_PRICE_ID}} \   -d "line_items[1][quantity]"=1 \  -d mode=subscription \   --data-urlencode success_url="https://example.com/success" \   --data-urlencode cancel_url="https://example.com/cancel"`

### Payment methods

You can view, enable, and disable different payment methods in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) at any time. Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. View our [complete list of payment methods](/payments/payment-methods/overview).

### Save payment details and default payment methods

You can [save payment details for future use](/payments/save-and-reuse) by sending an API parameter when you create a Session. Options to save payment details include:

*   **Single payment**: If your Checkout Session uses `payment` mode, set the [payment\_intent\_data.setup\_future\_usage](/payments/payment-intents#future-usage) parameter.
*   **Subscription payment**: If your Checkout Session uses `subscription` mode, Stripe saves the payment method by default.
*   [Multiple saved payment methods](/payments/accept-a-payment?platform=web&ui=checkout#save-payment-method-details): If a customer has multiple payment methods saved, you can store a default payment method to the Customer object’s [default\_payment\_method](/api/customers/object#customer_object-invoice_settings-default_payment_method) field. However, these payment methods don’t appear for return purchases in Checkout.

### Guest customers

The `Customer` object represents a customer of your business, and it helps tracking subscriptions and payments that belong to the same customer. Checkout Sessions that don’t create Customers are associated with [guest customers](/payments/checkout/guest-customers) instead.

Complete a transaction
----------------------

To automate business flows after a transaction has occurred, register an [event destination](/event-destinations) and build a [webhook endpoint handler](/webhooks/quickstart). Consider the following events and automations to enable:

*   Process the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event to fullfill orders when a customer completes their purchase.
*   Process the [checkout.session.expired](/api/events/types#event_types-checkout.session.expired) event to return items to your inventory or send users a cart [abandonment](/payments/checkout/abandoned-carts) email when they don’t make a purchase and their cart expires.

See also
--------

*   [Checkout quickstart](/checkout/quickstart)
*   [Fulfill your orders](/checkout/fulfillment)
*   [Collect taxes in Checkout](/payments/checkout/taxes)
*   [Manage limited inventory with Checkout](/payments/checkout/managing-limited-inventory)
*   [Automatically convert to local currencies with Adaptive Pricing](/payments/checkout/adaptive-pricing)

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Checkout lifecycle](#lifecycle "Checkout lifecycle")

[Low-code integration](#low-code "Low-code integration")

[Built-in and customizable features](#features "Built-in and customizable features")

[Built-in features](#built-in "Built-in features")

[Customizable features](#customizable "Customizable features")

[Custom branding](#branding "Custom branding")

[Custom domains](#custom-domains "Custom domains")

[Checkout Session](#session "Checkout Session")

[One-time and recurring payments](#checkout-mode "One-time and recurring payments")

[Mixed cart](#mixed-cart "Mixed cart")

[Payment methods](#payment-methods "Payment methods")

[Save payment details and default payment methods](#save-payment-methods "Save payment details and default payment methods")

[Guest customers](#guest-customers "Guest customers")

[Complete a transaction](#complete-transaction "Complete a transaction")

[See also](#see-also "See also")

Related Guides

[

No-code options to accept payments on Stripe



](/no-code)

[

Prebuilt checkout page



](/checkout/quickstart)

[

Learn about payment methods



](/payments/payment-methods/overview)

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/after-the-payment

 After the payment | Documentazione Stripe     

[Passa al contenuto](#main-content)

Dopo il pagamento

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fafter-the-payment)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fafter-the-payment)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

Dopo il pagamento

[Evadere gli ordini](/checkout/fulfillment)

[Send receipts and paid invoices](/payments/checkout/receipts)

[Personalizzare il comportamento di reindirizzamento](/payments/checkout/custom-success-page)

[Recuperare i carrelli abbandonati](/payments/checkout/abandoned-carts)

[Analizzare il funnel di conversione](/payments/checkout/analyze-conversion-funnel)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page

After the payment
=================

Customize the post-payment checkout process.
--------------------------------------------

[

Fulfill orders

Handle post-checkout tasks, such as fulfilling orders and shipping products.

](/checkout/fulfillment "Fulfill orders")

[

Customize redirect behavior

Display a confirmation page with your customer’s order information.

](/payments/checkout/custom-success-page "Customize redirect behavior")

[

Recover abandoned carts

Recover abandoned checkout pages and boost revenue.

](/payments/checkout/abandoned-carts "Recover abandoned carts")

[

Analyze your conversion funnel

Analyze your Stripe Checkout conversion funnel with Google Analytics 4.

](/payments/checkout/analyze-conversion-funnel "Analyze your conversion funnel")

[

Send email receipts and paid invoices

Send payment or refund receipts automatically.

](/payments/checkout/receipts "Send email receipts and paid invoices")

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/promotions

 Add discounts, upsells, and cross-sells | Documentación de Stripe     

[Ir a contenido](#main-content)

Añade descuentos y ventas adicionales y cruzadas

[

Crea una cuenta



](https://dashboard.stripe.com/register)o[

inicia sesión



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpromotions)

[

](/)

Busca en la documentación

/

[Crear cuenta](https://dashboard.stripe.com/register)

[

Iniciar sesión



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpromotions)

[

Empezar



](/get-started)

[

Pagos



](/payments)

[

Automatización de finanzas



](/finance-automation)

[

Plataformas y marketplaces



](/connect)

[

Banca como servicio



](/financial-services)

[

Herramientas para desarrolladores



](/development)

[

Empezar



](/get-started)

[

Pagos



](/payments)

[

Automatización de finanzas



](/finance-automation)

[

Empezar



](/get-started)

[

Pagos



](/payments)

[

Automatización de finanzas



](/finance-automation)

[

Plataformas y marketplaces



](/connect)

[

Banca como servicio



](/financial-services)

API y SDK

Ayuda

[Resumen](/payments)

Acerca de Stripe Payments

[Actualiza tu integración](/payments/upgrades "Mejora tu integración actual")

Análisis de pagos

Pagos por Internet

[Resumen](/payments/online-payments "Obtén información sobre las opciones de integración para aceptar pagos por Internet.")[Encuentra tu caso de uso](/payments/use-cases/get-started "Descubre cómo Stripe puede ayudar a tu empresa.")

Use Payment Links

Crear una página del proceso de compra

[Resumen](/payments/checkout/build-integration "Crea una experiencia de pagos con Checkout.")

[Guías de inicio rápido](/payments/checkout/quickstarts "Empieza con el código de muestra.")

[Personaliza el estilo](/payments/checkout/customization "Modifica la apariencia de tu página del proceso de compra. El nivel de personalización depende del producto que utilices.")

[Recolecta información adicional](/payments/checkout/collect-additional-info "Recolecta información como las direcciones de envío y los números de teléfono como parte del proceso de compra.")

[Cobrar impuestos](/payments/checkout/taxes)

[Actualiza forma dinámica el proceso de compra](/payments/checkout/dynamic-updates "Haz actualizaciones mientras tu cliente efectúa una compra.")

[Gestiona tu catálogo de productos](/payments/checkout/product-catalog)

[Suscripciones](/payments/subscriptions "Gestiona suscripciones con Checkout")

[Gestiona los métodos de pago](/payments/checkout/payment-methods)

[Permite que los clientes paguen en su divisa local](/payments/checkout/adaptive-pricing)

Añade descuentos y ventas adicionales y cruzadas

[Añadir descuentos](/payments/checkout/discounts)

[Configurar las ventas de productos de más valor de suscripciones](/payments/checkout/upsells)

[Configurar ventas cruzadas](/payments/checkout/cross-sells)

[Deja que los clientes completen pedidos de forma gratuita](/payments/checkout/no-cost-orders)

[Mostrar precios anuales en términos mensuales](/payments/checkout/yearly-price-display)

[Configurar pagos futuros](/payments/checkout/save-and-reuse "Descubre cómo guardar los datos de pago para cobrarles a tus clientes más tarde")

[Guardar datos de pago durante el pago](/payments/checkout/save-during-payment "Guardar datos de pago durante el pago")

[Después del pago](/payments/checkout/after-the-payment)

[Elements con el registro de cambios de la API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrar desde Checkout heredado](/payments/checkout/migration)

[Migrar Checkout para usar precios](/payments/checkout/migrating-prices)

Desarrolla una integración avanzada

Desarrolla una integración en la aplicación

Métodos de pago

Añadir métodos de pago

Gestiona los métodos de pago

Proceso de compra más rápido con Link

Interfaces de usuario de pagos

Payment Links

Checkout

Elements para la web

Elements en la aplicación

Escenarios de pago

Flujos de pagos personalizados

Capacidad adquirente flexible

Pagos en persona

Terminal

Otros productos de Stripe

Financial Connections

Criptomonedas

Climate

Enlaces de transferencia

España

Español (España)

[Inicio](/ "Inicio")[Pagos](/payments "Pagos")Build a checkout page

Add discounts, upsells, and cross-sells
=======================================

Boost sales with discounts and offers.
--------------------------------------

[

Add discounts

Reduce the amount charged to a customer by discounting their subtotal with coupons and promotion codes.

](/payments/checkout/discounts "Add discounts")

[

Configure free trials

Offer customer free trials on subscriptions.

](/payments/checkout/free-trials "Configure free trials")

[

Configure subscription upsells

Enable customers to upgrade their subscription plan at checkout by using upsells.

](/payments/checkout/upsells "Configure subscription upsells")

[

Configure cross-sells

Enable customers to purchase complementary products at checkout by using cross-sells.

](/payments/checkout/cross-sells "Configure cross-sells")

[

Let customers complete orders for free

Accept orders for no-cost line items, and apply 100% off discounts in payment mode.

](/payments/checkout/no-cost-orders "Let customers complete orders for free")

¿Te ha sido útil la página?

SíNo

¿Necesitas ayuda? [Ponte en contacto con el equipo de soporte](https://support.stripe.com/).

Únete a nuestro [programa de acceso anticipado](https://insiders.stripe.dev/).

Consulta nuestro [registro de cambios de productos](https://stripe.com/blog/changelog).

¿Tienes alguna pregunta? [Ponte en contacto con el equipo de ventas](https://stripe.com/contact/sales).

Con tecnología de [Markdoc](https://markdoc.dev)

Inscríbete para recibir las actualizaciones para desarrolladores:

Inscríbete

Puedes cancelar la suscripción en cualquier momento. Consulta nuestra [Política de privacidad](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La experiencia con Stripe Shell es mejor en ordenadores de sobremesa.

    $

---

## URL: https://docs.stripe.com/payments/checkout/save-during-payment

 Save payment details during payment | Documentazione Stripe     

[Passa al contenuto](#main-content)

Salvare i dati di pagamento durante il pagamento

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fsave-during-payment)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fsave-during-payment)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

Salvare i dati di pagamento durante il pagamento

[Clienti ospiti](/payments/checkout/guest-customers)

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page

Save payment details during payment
===================================

Learn how to accept a payment and save your customer's payment details for future purchases.
--------------------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Use [Stripe Checkout](/payments/checkout) for a fast, low-code integration that allows your customers to save their payment details for future purchases.

[

Set up Stripe

Server-side




------------------------------





](#set-up-stripe)

First, [register](https://dashboard.stripe.com/register) for a Stripe account.

Use our official libraries to access the Stripe API from your application:

Command Line

Ruby

`# Available as a gem sudo gem install stripe`

Gemfile

Ruby

`# If you use bundler, you can add this line to your Gemfile gem 'stripe'`

[

Create a customer

Server-side




----------------------------------





](#create-a-customer)

To set a card up for future payments, you must attach it to a [Customer](/api/customers "Clienti"). Create a Customer object when your customer creates an account with your business. Customer objects allow for reusing payment methods and tracking across multiple payments.

Command Line

cURL

`curl https://api.stripe.com/v1/customers \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d name="Jenny Rosen" \   --data-urlencode email="jennyrosen@example.com"`

Successful creation returns the [Customer](/api/customers/object) object. You can inspect the object for the customer `id` and store the value in your database for later retrieval.

You can find these customers in the [Customers](https://dashboard.stripe.com/customers) page in the Dashboard.

[

Create a Checkout Session

Client-side

Server-side




-------------------------------------------------------





](#create-checkout-session)

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](/api/checkout/sessions/create).

You can also create a Checkout Session for an [existing customer](/payments/existing-customers?platform=web&ui=stripe-hosted), allowing you to prefill Checkout fields with known contact information and unify your purchase history for that customer.

checkout.html

`<html>   <head>     <title>Buy cool new product</title>   </head>   <body>     <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->     <form action="/create-checkout-session" method="POST">       <button type="submit">Checkout</button>     </form>   </body> </html>`

A Checkout Session is the programmatic representation of what your customer sees when they’re redirected to the payment form. You can configure it with options such as:

*   [Line items](/api/checkout/sessions/create#create_checkout_session-line_items) to charge
*   Currencies to use

You must populate `success_url` with the URL value of a page on your website that Checkout returns your customer to after they complete the payment. You can optionally also provide a `cancel_url` value of a page on your website that Checkout returns your customer to if they terminate the payment process before completion.

#### Nota

Checkout Sessions expire 24 hours after creation by default.

After creating a Checkout Session, redirect your customer to the [URL](/api/checkout/sessions/object#checkout_session_object-url) returned in the response.

Ruby

`# This example sets up an endpoint using the Sinatra framework. # Watch this video to get started: [https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)  require 'json' require 'sinatra' require 'stripe'  # Set your secret key. Remember to switch to your live secret key in production. # See your keys here: [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys) Stripe.api_key =   'sk_test_9W1R4v0cz6AtC9PVwHFzywti'  post '/create-checkout-session' do   session = Stripe::Checkout::Session.  create  ({     line_items: [{       price_data: {         currency: 'usd',         product_data: {           name: 'T-shirt',         },         unit_amount: 2000,       },       quantity: 1,     }],     mode: 'payment',     # These placeholder URLs will be replaced in a following step.     success_url: '[https://example.com/success](https://example.com/success)',     cancel_url: '[https://example.com/cancel](https://example.com/cancel)',   })    redirect session.url, 303 end`

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn individual payment methods on or off in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). By default, Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe filters them out even when they’re enabled. We filter Google Pay if you [enable automatic tax](/tax/checkout) without collecting a shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

### Confirm your endpoint

Confirm your endpoint is accessible by starting your web server (for example, `localhost:4242`) and running the following command:

Command Line

`curl -X POST -is "http://localhost:4242/create-checkout-session" -d ""`

You should see a response in your terminal that looks like this:

Command Line

`HTTP/1.1 303 See Other Location: [https://checkout.stripe.com/c/pay/cs_test_...](https://checkout.stripe.com/c/pay/cs_test_..) ...`

### Testing

You should now have a working checkout button that redirects your customer to Stripe Checkout.

1.  Click the checkout button.
2.  You’re redirected to the Stripe Checkout payment form.

If your integration isn’t working:

1.  Open the Network tab in your browser’s developer tools.
2.  Click the checkout button and confirm it sent an XHR request to your server-side endpoint (`POST /create-checkout-session`).
3.  Verify the request is returning a 200 status.
4.  Use `console.log(session)` inside your button click listener to confirm the correct data returned.

For more information about configuring and testing your hosted Checkout integration, see [Accept a Payment](/payments/accept-a-payment?platform=web&ui=hosted-form).

[

Save payment method

Server-side




------------------------------------





](#save-payment-method)

After setting up your hosted Checkout integration, choose a configuration for your integration to save the payment methods used by your customers.

By default, payment methods used to make a one-time payment with Checkout aren’t available for future use.

### Save payment methods to charge them off-session

You can set Checkout to save payment methods used to make a one-time payment by passing the [payment\_intent\_data.setup\_future\_usage](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage) argument. This is useful if you need to capture a payment method on-file to use for future fees, such as cancellation or no-show fees.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d customer_creation=always \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][unit_amount]"=2000 \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success.html](https://example.com/success.html)" \   --data-urlencode cancel_url="[https://example.com/cancel.html](https://example.com/cancel.html)" \  -d "payment_intent_data[setup_future_usage]"=off_session`

If you use Checkout in `subscription` mode, Stripe automatically saves the payment method to charge it for subsequent payments. Card payment methods saved to customers using either `setup_future_usage` or `subscription` mode don’t appear for return purchases in Checkout (more on this below). We recommend using [custom text](/payments/checkout/customization/policies) to link out to any relevant terms regarding the usage of saved payment information.

#### Attenzione

Global privacy laws are complicated and nuanced. We recommend contacting your legal and privacy team prior to implementing [setup\_future\_usage](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage) because it might implicate your existing privacy compliance framework. Refer to [the guidance issued by the European Protection Board](https://edpb.europa.eu/system/files/2021-05/recommendations022021_on_storage_of_credit_card_data_en_1.pdf) to learn more about saving payment details.

### Save payment methods to prefill them in Checkout

By default, Checkout uses [Link](/payments/checkout/customization/behavior#link) to provide your customers with the option to securely save and reuse their payment information. If you prefer to manage payment methods yourself, use [saved\_payment\_method\_options.payment\_method\_save](/api/checkout/sessions/create#create_checkout_session-saved_payment_method_options-payment_method_save) when creating a Checkout Session to let your customers save their payment methods for future purchases in Checkout.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d customer_creation=always \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][unit_amount]"=2000 \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success.html](https://example.com/success.html)" \   --data-urlencode cancel_url="[https://example.com/cancel.html](https://example.com/cancel.html)" \  -d "saved_payment_method_options[payment_method_save]"=enabled`

Passing this parameter in either [payment](/api/checkout/sessions/create#create_checkout_session-mode) or [subscription](/api/checkout/sessions/create#create_checkout_session-mode) mode displays an optional checkbox to let customers explicitly save their payment method for future purchases. When customers check this checkbox, Checkout saves the payment method with [allow\_redisplay: always](/api/payment_methods/object#payment_method_object-allow_redisplay). Checkout uses this parameter to determine whether a payment method can be prefilled on future purchases. When using `saved_payment_method_options.payment_method_save`, you don’t need to pass in `setup_future_usage` to save the payment method.

Using [saved\_payment\_method\_options.payment\_method\_save](/api/checkout/sessions/create#create_checkout_session-saved_payment_method_options-payment_method_save) requires a `Customer`. To save a new customer, set the Checkout Session’s [customer\_creation](/api/checkout/sessions/create) to `always`. Otherwise, the session doesn’t save the customer or the payment method.

If `payment_method_save` isn’t passed in or if the customer doesn’t agree to save the payment method, Checkout still saves payment methods created in `subscription` mode or using `setup_future_usage`. These payment methods have an `allow_redisplay` value of `limited`, which prevents them from being prefilled for returning purchases and allows you to comply with card network rules and data protection regulations. Learn how to [change the default behavior enabled by these modes](https://support.stripe.com/questions/prefilling-saved-cards-in-checkout) and how to change or override `allow_redisplay` behavior.

#### Nota

You can use Checkout to save cards and other payment methods to charge them off-session, but Checkout only prefills saved cards. Learn how to [prefill saved cards](https://support.stripe.com/questions/prefilling-saved-cards-in-checkout). To save a payment method without an initial payment, [use Checkout in setup mode](/payments/save-and-reuse?platform=checkout).

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Set up Stripe](#set-up-stripe "Set up Stripe")

[Create a customer](#create-a-customer "Create a customer")

[Create a Checkout Session](#create-checkout-session "Create a Checkout Session")

[Payment methods](#payment-methods "Payment methods")

[Confirm your endpoint](#confirm-your-endpoint "Confirm your endpoint")

[Testing](#redirect-stripe-checkout-testing "Testing")

[Save payment method](#save-payment-method "Save payment method")

[Save payment methods to charge them off-session](#save-payment-methods-to-charge-them-off-session "Save payment methods to charge them off-session")

[Save payment methods to prefill them in Checkout](#save-payment-methods-to-prefill-them-in-checkout "Save payment methods to prefill them in Checkout")

Prodotti utilizzati

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/product-catalog

 Manage your product catalog | Stripe Documentation     

[Skip to content](#main-content)

Manage your product catalog

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fproduct-catalog)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fproduct-catalog)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

Manage your product catalog

[Manage limited inventory](/payments/checkout/managing-limited-inventory)

[Make line item quantities adjustable](/payments/checkout/adjustable-quantity)

[Let customers decide what to pay](/payments/checkout/pay-what-you-want)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Singapore

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

Manage your product catalog
===========================

Handle your inventory and fulfillment.
--------------------------------------

[

Manage limited inventory

Prevent customers from holding inventory in carts by expiring Checkout Sessions.

](/payments/checkout/managing-limited-inventory "Manage limited inventory")

[

Make line item quantities adjustable

Configure the Checkout Session so customers can adjust line item quantity during checkout.

](/payments/checkout/adjustable-quantity "Make line item quantities adjustable")

[

Dynamically update line items

Update the line items during the Checkout Session with your own custom logic.

](/payments/checkout/dynamically-update-line-items "Dynamically update line items")

[

Let customers decide what to pay

Accept tips and donations, or sell pay-what-you-want products and services.

](/payments/checkout/pay-what-you-want "Let customers decide what to pay")

[

Limit customers to one subscription

Prevent customers from unintentionally creating multiple subscriptions.

](/payments/checkout/limit-subscriptions "Limit customers to one subscription")

[

Set billing cycle date

Set the billing cycle anchor date for subscriptions.

](/payments/checkout/billing-cycle "Set billing cycle date")

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/receipts

 Email receipts and paid invoices | Documentação da Stripe     

[Pular para o conteúdo](#main-content)

Send receipts and paid invoices

[

Criar conta



](https://dashboard.stripe.com/register)ou[

Entrar



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Freceipts)

[

](/)

Pesquise a documentação

/

[Criar conta](https://dashboard.stripe.com/register)

[

Login



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Freceipts)

[

Comece já



](/get-started)

[

Pagamentos



](/payments)

[

Automação de finanças



](/finance-automation)

[

Plataformas e marketplaces



](/connect)

[

Banco como serviço



](/financial-services)

[

Ferramentas para desenvolvedores



](/development)

[

Comece já



](/get-started)

[

Pagamentos



](/payments)

[

Automação de finanças



](/finance-automation)

[

Comece já



](/get-started)

[

Pagamentos



](/payments)

[

Automação de finanças



](/finance-automation)

[

Plataformas e marketplaces



](/connect)

[

Banco como serviço



](/financial-services)

APIs e SDKs

Ajuda

[Visão geral](/payments)

Sobre os pagamentos da Stripe

[Atualize sua integração](/payments/upgrades "Melhore sua integração existente")

Análise de pagamentos

Pagamentos online

[Visão geral](/payments/online-payments "Conheça as opções de integração para receber pagamentos online.")[Encontre seu caso de uso](/payments/use-cases/get-started "Saiba como a Stripe pode apoiar a sua empresa.")

Use Payment Links

Crie uma página de checkout

[Visão geral](/payments/checkout/build-integration "Crie uma experiência de pagamentos com o Checkout.")

[Inícios rápidos](/payments/checkout/quickstarts "Comece com um exemplo de código.")

[Personalizar a aparência](/payments/checkout/customization "Controle a aparência da sua página de checkout. O nível de personalização depende do produto que você utiliza.")

[Coletar informações adicionais](/payments/checkout/collect-additional-info "Colete informações como endereços de entrega e números de telefone como parte do processo de checkout.")

[Colete impostos](/payments/checkout/taxes)

[Atualizar checkout dinamicamente](/payments/checkout/dynamic-updates "Faça atualizações enquanto seu cliente faz o checkout.")

[Gerencie seu catálogo de produtos](/payments/checkout/product-catalog)

[Assinaturas](/payments/subscriptions "Gerenciar assinaturas com o Checkout")

[Gerenciar formas de pagamento](/payments/checkout/payment-methods)

[Permita que os clientes paguem na moeda local](/payments/checkout/adaptive-pricing)

[Adicionar descontos, upsells e vendas cruzadas](/payments/checkout/promotions)

[Configurar pagamentos futuros](/payments/checkout/save-and-reuse "Aprenda a salvar dados do pagamento e cobrar o cliente depois")

[Salvar dados de pagamento durante o pagamento](/payments/checkout/save-during-payment "Salvar dados de pagamento durante o pagamento")

[Após o pagamento](/payments/checkout/after-the-payment)

[Executar pedidos](/checkout/fulfillment)

Send receipts and paid invoices

[Personalizar o comportamento de redirecionamento](/payments/checkout/custom-success-page)

[Recupere carrinhos abandonados](/payments/checkout/abandoned-carts)

[Analisar funil de conversão](/payments/checkout/analyze-conversion-funnel)

[Elements com changelog da API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrar do Checkout antigo](/payments/checkout/migration)

[Migrar o Checkout para usar Prices](/payments/checkout/migrating-prices)

Criar uma integração avançada

Crie uma integração no aplicativo

Formas de pagamento

Adicionar formas de pagamento

Gerenciar formas de pagamento

Checkout mais rápido com o Link

IUs de pagamento

Payment Links

Checkout

Web Elements

Elements no aplicativo

Cenários de pagamento

Fluxos de pagamento personalizados

Aquisição flexível

Pagamentos presenciais

Terminal

Outros produtos da Stripe

Financial Connections

Cripto

Climate

Links de repasse

Brasil

Português (Brasil)

[Página inicial](/ "Página inicial")[Pagamentos](/payments "Pagamentos")Build a checkout page[After the payment](/payments/checkout/after-the-payment "After the payment")

Email receipts and paid invoices
================================

Send receipts for payments and refunds automatically.
-----------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

You can manually or automatically send customized email receipts or [paid invoices](#paid-invoices). Learn more about [receipts for payments](/receipts).

Automatically send receipts
---------------------------

To enable automated receipts, toggle **Successful payments** on in your [Customer emails settings](https://dashboard.stripe.com/settings/emails). Receipts are only sent when a successful payment has been made—no receipt is sent if the payment fails or is declined.

Customize receipts
------------------

Alter the appearance and functionality of your receipts with the following customization options:

*   **Branding**: Modify the logo and colors in your [Branding settings](https://dashboard.stripe.com/settings/branding). The upper limit for a custom logo image file size is 512KB. Ideally, the logo should be a square image exceeding 128 x 128 pixels. JPG, PNG, and GIF file types are supported.
*   **Public information**: Specify the public information you want to include, such as your contact number or website address, in your [Public details settings](https://dashboard.stripe.com/settings/public).

To display custom text, use the [payment\_intent\_data.description](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-description) attribute on the [Checkout Session](/api/checkout/sessions/object). Some examples include:

*   Description of goods or services provided
*   Authorization code
*   Subscription information
*   Cancellation policies

You can see a real-time preview of your email receipt on your Dashboard Branding settings page. To send a test receipt, hover over the preview image and click **Send test receipt**, then enter your email address.

#### Cuidado

Receipts pull data from the `Charge` object generated when the PaymentIntent is confirmed. To update receipt data such as the `description` after the charge is generated, you must [update the Charge](/api/charges/update). Changes to a confirmed PaymentIntent don’t appear on receipts.

Automatically send paid invoices
--------------------------------

In addition to ordinary receipts, Checkout can generate paid invoices as proof of payment. Invoices have more information than receipts. For subscriptions, Stripe generates invoices automatically, but for one-time payments, you need to enable them.

#### Observação

Invoice creation for one-time payments in Checkout is not an [Invoicing](https://stripe.com/invoicing) feature, and is priced separately. Review [this support article](https://support.stripe.com/questions/pricing-for-post-payment-invoices-for-one-time-purchases-via-checkout-and-payment-links) to learn more.

To generate invoices, first, in your [Customer emails settings](https://dashboard.stripe.com/settings/emails), under **Email customers about**, select **Successful payments**. Then, when creating a Checkout session, set [invoice\_creation\[enabled\]](/api/checkout/sessions/create#create_checkout_session-invoice_creation-enabled) to `true`.

#### Observação

Enabling `invoice_creation` isn’t supported if you set `payment_intent_data[capture_method]` to `manual`.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Ho24N7La5CVDtbmpjc377lJI  :" \  -d mode=payment \  -d "invoice_creation[enabled]"=true \  -d "line_items[0][price]"={{ONE_TIME_PRICE_ID}} \   -d "line_items[0][quantity]"=1 \   --data-urlencode success_url="https://example.com" \   --data-urlencode cancel_url="https://example.com"`

After the payment completes, Stripe sends an invoice summary with links to download the invoice PDF and invoice receipt to the email address your customer provides during checkout.

#### Cuidado

Invoices for delayed notification payment methods might take longer to send because we send the invoice after successful payment, not upon checkout session completion. These methods include: [Bacs Direct Debit](/payments/bacs-debit/accept-a-payment), [Bank transfers](/payments/bank-transfers/accept-a-payment), [Boleto](/payments/boleto/accept-a-payment), [Canadian pre-authorized debits](/payments/acss-debit/accept-a-payment), [Konbini](/payments/konbini/accept-a-payment), [OXXO](/payments/oxxo/accept-a-payment), [Pay by Bank](/payments/pay-by-bank/accept-a-payment), [SEPA Direct Debit](/payments/sepa-debit/accept-a-payment), [SOFORT](/payments/sofort/accept-a-payment), and [ACH Direct Debit](/payments/ach-direct-debit/accept-a-payment).

![Screenshot of the invoice PDF that customers can download from the invoice summary email](https://b.stripecdn.com/docs-statics-srv/assets/invoice.9e44668032383601eeec362f38293b7a.png)

The downloadable invoice PDF

![Screenshot of the invoice receipt that customers can download from the invoice summary email](https://b.stripecdn.com/docs-statics-srv/assets/invoice_receipt.4f120ee7363f8e7728fa553a8a24aae3.png)

The downloadable invoice receipt

![Screenshot of the invoice summary email Stripe sends](https://b.stripecdn.com/docs-statics-srv/assets/email.560c2666905531b907f7fcd4f1a0a6dd.png)

The customer email with links to the invoice PDF and receipt

You can also view the invoice in the [Dashboard](https://dashboard.stripe.com/invoices) or access it programmatically by listening to the [invoice.paid](/api/events/types#event_types-invoice.paid) event through an [event destination](/event-destinations).

You can use the `invoice_data` hash inside `invoice_creation` to further customize the invoice generated by the Checkout Session.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Ho24N7La5CVDtbmpjc377lJI  :" \  -d mode=payment \  -d "invoice_creation[enabled]"=true \  -d "invoice_creation[invoice_data][description]"="Invoice for Product X" \  -d "invoice_creation[invoice_data][metadata][order]"=order-xyz \  -d "invoice_creation[invoice_data][account_tax_ids][0]"=DE123456789 \  -d "invoice_creation[invoice_data][custom_fields][0][name]"="Purchase Order" \  -d "invoice_creation[invoice_data][custom_fields][0][value]"=PO-XYZ \  -d "invoice_creation[invoice_data][rendering_options][amount_tax_display]"=include_inclusive_tax \  -d "invoice_creation[invoice_data][footer]"="B2B Inc." \  -d "line_items[0][price]"={{ONE_TIME_PRICE_ID}} \   -d "line_items[0][quantity]"=1 \   --data-urlencode success_url="https://example.com" \   --data-urlencode cancel_url="https://example.com"`

Review [invoice best practices](/invoicing/global-invoicing) for your region to make sure you’re collecting the right information from your customers. Information like the customer’s billing and shipping addresses, phone number and tax ID appear on the resulting invoice.

Localization
------------

When using Checkout Sessions, the language of the receipt and invoice is determined by several factors:

*   If a Customer is set, their [preferred locale](/api/customers/object#customer_object-preferred_locales) are used if available.
*   If a Customer is set without any preferred locales, the [language setting](https://dashboard.stripe.com/settings/emails) from the Stripe Dashboard is applied.
*   If no Customer is set, the language defaults to the browser locale of the user opening the Checkout Session URL.

Veja também
-----------

*   [Send customer emails](/invoicing/send-email)
*   [Automate customer emails](/billing/revenue-recovery/customer-emails)

Esta página foi útil?

SimNão

Precisa de ajuda? [Fale com o suporte](https://support.stripe.com/).

Participe do nosso [programa de acesso antecipado](https://insiders.stripe.dev/).

Confira o [log de alterações do produto](https://stripe.com/blog/changelog).

Dúvidas? [Fale com a equipe de vendas](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Assine as atualizações para desenvolvedores:

Inscrever-se

Cancele o recebimento quando quiser. Leia a nossa [política de privacidade](https://stripe.com/privacy).

Nesta página

[Automatically send receipts](#automatically-send-receipts "Automatically send receipts")

[Customize receipts](#customizing-receipts "Customize receipts")

[Automatically send paid invoices](#paid-invoices-hosted "Automatically send paid invoices")

[Localization](#localization "Localization")

[Veja também](#see-also "Veja também")

Produtos usados

[

Payments





](/payments)

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

O Stripe Shell oferece uma melhor experiência em desktops.

    $

---

## URL: https://docs.stripe.com/payments/checkout/no-cost-orders

 No-cost orders | Stripe Documentation     

[Skip to content](#main-content)

Let customers complete orders for free

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fno-cost-orders)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fno-cost-orders)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Add discounts](/payments/checkout/discounts)

[Configure subscription upsells](/payments/checkout/upsells)

[Configure cross-sells](/payments/checkout/cross-sells)

Let customers complete orders for free

[Display yearly prices in monthly terms](/payments/checkout/yearly-price-display)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Add discounts, upsells, and cross-sells](/payments/checkout/promotions "Add discounts, upsells, and cross-sells")

No-cost orders
==============

Accept orders for no-cost line items or apply 100% off discounts for one-time payments.
---------------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

You can process no-cost orders for one-time payments with [no-cost line items](#no-cost-line-items) or discounts for 100% off with [coupons and customer-facing promotion codes](#full-cost-discounts).

#### Note

You must be on API version [2023-08-16](/upgrades#2023-08-16) or later to process no-cost orders using the Checkout Sessions API.

Create a Checkout Session with no-cost line items
-------------------------------------------------

Create a [Price](/api/prices) with a [unit\_amount](/api/prices/object#price_object-unit_amount) of 0, and pass it into the [line items](/api/checkout/sessions/line_items) array of the Checkout Session. See [Products and prices](/invoicing/products-prices) for more information on creating prices.

You can also use the [price\_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data) parameter of the `line_items` array to pass in a free price.

If the total amount is 0, Checkout doesn’t collect a payment method from the customer.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price_data][unit_amount]"=0 \  -d "line_items[0][price_data][product_data][name]"="Free t-shirt" \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

If the `customer` property isn’t set, the Checkout Session automatically creates a new Customer object. This means [guest customers](/payments/checkout/guest-customers) aren’t supported.

Create a discount
-----------------

Alternatively, create a coupon and a promotion code to allow customers to complete orders for free.

### Create a coupon

Create a [Coupon](/api/coupons) that makes your Checkout Session free. For example, you can create a 100% off coupon.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/coupons \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d percent_off=100 \  -d duration=once`

To create a session with an applied discount, pass the [coupon ID](/api/coupons/object#coupon_object-id) in the `coupon` parameter of the [discounts](/api/checkout/sessions/create#create_checkout_session-discounts) array.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price_data][unit_amount]"=2000 \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][quantity]"=1 \  -d "discounts[0][coupon]"=  {{COUPON_ID}}   \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

You can also create a free Checkout Session by applying a coupon for an amount equal to or exceeding the Checkout Session total.

### Create a promotion code

Promotion codes are customer-facing codes created on top of coupons. You can share these codes with customers who can enter them into Checkout to apply a discount. Create a promotion code from a 100% off coupon to allow customers to create orders for free.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/promotion_codes \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d coupon=  {{COUPON_ID}}   \  -d code=FREECODE`

Enable user-redeemable promotion codes using the [allow\_promotion\_codes](/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes) parameter in a Checkout Session. This enables a field in Checkout to allow users to enter promotion codes.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price_data][unit_amount]"=2000 \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][quantity]"=1 \  -d mode=payment \  -d allow_promotion_codes=true \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

Customers can also check out for free if they apply a promotion code for an amount equal to or exceeding the Checkout Session total. For more ways to apply discounts, see [Add discounts](/payments/checkout/discounts).

Handle completed orders
-----------------------

After the Checkout Session completes, you can make a request for the finalized [line items](/api/checkout/sessions/line_items) and their quantities. If your customer removes a line item, it also removes it from the line items response. See the [Fulfillment guide](/checkout/fulfillment) to learn how to create an event handler to handle completed Checkout Sessions.

#### Common mistake

To fulfill no-cost orders, make sure to handle the `checkout.session.completed` event rather than [PaymentIntent](/payments/payment-intents) events. Completed Checkout Sessions that are free won’t have an associated [PaymentIntent](/payments/payment-intents).

You can see your completed no-cost orders in the [Dashboard](https://dashboard.stripe.com/no-cost-orders). The no-cost orders tab only appears if you have at least one completed no-cost order.

[

OptionalPayment links and pricing tables


------------------------------------------





](#payment-links-and-pricing-tables)

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Create a Checkout Session with no-cost line items](#no-cost-line-items "Create a Checkout Session with no-cost line items")

[Create a discount](#full-cost-discounts "Create a discount")

[Create a coupon](#create-a-coupon "Create a coupon")

[Create a promotion code](#create-a-promotion-code "Create a promotion code")

[Handle completed orders](#handling-orders "Handle completed orders")

Products Used

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/compliant-promotional-emails

 Compliant promotional emails | Stripe 文档     

[调至内容部分](#main-content)

合规促销邮件

[

创建账户



](https://dashboard.stripe.com/register)或[

登录



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcompliant-promotional-emails)

[

](/)

搜索文档

/

[创建账户](https://dashboard.stripe.com/register)

[

登录



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcompliant-promotional-emails)

[

开始



](/get-started)

[

付款



](/payments)

[

财务自动化



](/finance-automation)

[

平台和交易市场



](/connect)

[

银行即服务



](/financial-services)

[

开发人员工具



](/development)

[

开始



](/get-started)

[

付款



](/payments)

[

财务自动化



](/finance-automation)

[

开始



](/get-started)

[

付款



](/payments)

[

财务自动化



](/finance-automation)

[

平台和交易市场



](/connect)

[

银行即服务



](/financial-services)

API 和 SDK

帮助

[概览](/payments)

关于 Stripe 支付

[升级您的集成应用](/payments/upgrades "改进现有集成")

支付分析

线上付款

[概览](/payments/online-payments "了解在线收款的集成选项。")[查找您的用例](/payments/use-cases/get-started "了解 Stripe 如何能支持您的业务。")

Use Payment Links

构建结账页面

[概览](/payments/checkout/build-integration "用 Checkout 构建支付体验。")

[快速开始](/payments/checkout/quickstarts "使用实例代码开始。")

[自定义外观样式](/payments/checkout/customization "控制结账页面的外观。自定义级别取决于您使用的产品。")

[收集额外信息](/payments/checkout/collect-additional-info "在结账过程中收集客户的收货地址和电话号码等信息。")

[收集物理地址](/payments/collect-addresses "了解如何收集账单地址和收货地址。")

[收取运费](/payments/during-payment/charge-shipping)

[收集电话号码](/payments/checkout/phone-numbers "使用 Checkout 收集客户的电话号码")

[添加自定义字段](/payments/checkout/custom-fields)

[收集促销邮件通知许可](/payments/checkout/promotional-emails-consent)

合规促销邮件

[收税](/payments/checkout/taxes)

[动态更新结账流程](/payments/checkout/dynamic-updates "在客户结账过程中进行更新")

[管理产品目录](/payments/checkout/product-catalog)

[订阅](/payments/subscriptions "用 Checkout 管理订阅")

[管理支付方式](/payments/checkout/payment-methods)

[让客户用本地货币支付](/payments/checkout/adaptive-pricing)

[添加折扣、追加销售和交叉销售](/payments/checkout/promotions)

[设置未来付款](/payments/checkout/save-and-reuse "了解如何保存支付详情并在将来对客户扣款")

[支付过程中保存付款详情](/payments/checkout/save-during-payment "支付过程中保存付款详情")

[付款后](/payments/checkout/after-the-payment)

[具有 Checkout Sessions API 更改日志的 Element](/checkout/elements-with-checkout-sessions-api/changelog)

[从传统 Checkout 迁移](/payments/checkout/migration)

[迁移 Checkout 来使用 Prices](/payments/checkout/migrating-prices)

构建高级集成应用

构建应用内集成

支付方式

添加支付方式

管理支付方式

用 Link 更快结账

支付 UI

Payment Link

结账

Web Elements

应用内 Element

支付场景

自定义支付流程

灵活收单

线下支付

Terminal

其他 Stripe 产品

Financial Connections

加密货币

Climate

提现链接

马来西亚

简体中文

[首页](/ "首页")[付款](/payments "付款")Build a checkout page[Collect additional information](/payments/checkout/collect-additional-info "Collect additional information")[Collect consent for promotional emails](/payments/checkout/promotional-emails-consent "Collect consent for promotional emails")

Compliant promotional emails
============================

Follow these best practices to ensure compliant promotional emails.
-------------------------------------------------------------------

[Promotional emails](/payments/checkout/promotional-emails-consent) promote a product or service (for example, recovery emails, newsletters, or promotions) and represent an opportunity to strengthen and expand your relationship with customers. Read through these best practices for enabling compliance, but be aware of laws that restrict your ability to use your customers’ personal data for promotional content—check with your legal counsel if you’re unsure.

Privacy and marketing laws require companies to notify or gain consent from customers before sending promotional emails and promptly honor unsubscribe requests.

#### 注意

Review the callouts which may require specific updates to your documentation or practices.

Customer consent
----------------

Checkout helps you optimize collection of customer opt-in and opt-out permissions.

The laws around consent to use personal data such as emails to send promotional messages differ by country. For US merchants and customers, laws generally allow sending promotional messages as long as you offer an opt-out opportunity and honor any unsubscribe requests that you have received. Many rest of world jurisdictions require an affirmative consent flow.

When you enable promotional emails, Checkout presents a checkbox beneath the email field that reads “Keep me updated with news and personalized offers.” It can be unclear which country’s laws apply to a particular transaction. Because of this, Stripe uses logic that considers both the jurisdiction of your Stripe account and the IP address of the customer to determine whether the default is for the checkbox to be checked or unchecked. When our logic determines that either your Stripe account or the customer is located in a jurisdiction that requires (or is otherwise advisable to obtain) affirmative consent, by default, we present such customers with the unchecked checkbox.

This feature can also help you send [abandoned cart or “recovery"](/payments/checkout/abandoned-carts) emails, which are encouraging emails sent to customers who almost made a purchase. In the case of recovery emails, you only receive the email addresses of prospective customers who’ve entered their email addresses into your checkout form and have given permission to receive promotional emails (that is, the email address is validated and the checkbox is checked when the checkout session expires). We recommend that you use these emails only for sending recovery emails and limit targeting broader marketing campaigns to customers who have successfully completed a purchase and provided consent.

In either case, if the customer notifies you that they don’t want to receive promotional content or you have another reason to believe they don’t want their personal data used to send promotional emails, don’t send the emails, despite the permission provided from Checkout.

Customer unsubscribe requests
-----------------------------

#### 注意

Ensure consumers can unsubscribe and requests are promptly honored.

All promotional emails must include information about the sender and a way for customers to unsubscribe, and you must promptly honor all unsubscribe requests. [Customers](/api/customers "客户") who have unsubscribed shouldn’t receive promotional emails unless they subsequently express consent. To make sure you meet requirements in your jurisdiction, provide customers the opportunity to withdraw their consent or unsubscribe to future marketing content directly from your website or an easily-accessible customer service process. The process for withdrawing consent should be as easy as providing consent.

If a customer reaches out to Stripe with a request to delete their personal information or to stop using it for promotional purposes, Stripe won’t act on that request. Stripe acts as a service provider/processor to you, and will treat these unsubscribe requests like other “data subject requests” that Stripe receives regarding your customers. Stripe will redirect the customer back to you to respond to, and honor, their requests.

Privacy policy update
---------------------

#### 注意

Update your privacy to disclose data collection and usage for promotional emails.

As outlined in our [Terms of Service](https://stripe.com/legal), you must disclose the collection and use of your customers’ data for sending promotional emails in your privacy policy or other privacy notices. Because of the limited use rights obtained in this checkbox, you may not use the information provided through this feature for any purposes beyond sending news and promotional emails unless you explicitly obtain those rights outside of this feature in Checkout.

Checkout’s privacy policy, which is linked on every Checkout session, discloses that Stripe collects information solely as a service provider to the merchant and isn’t an independent controller of customer data. We recommend that you also review your privacy policy before using this feature. Your privacy policy should disclose to customers all the ways you collect, retain, use, and share data—this includes the data you collect through Checkout from prospective customers who visit your webpage but don’t complete a transaction. It would be advisable to also disclose that you may send them promotional emails based on their opt-in or opt-out selection during checkout. See the [Stripe Privacy Center](https://stripe.com/privacy-center/legal) for more information.

此页面的内容有帮助吗？

是否

需要帮助？[联系支持](https://support.stripe.com/)。

加入我们的[早期使用计划](https://insiders.stripe.dev/)。

查看我们的[产品更改日志](https://stripe.com/blog/changelog)。

有问题？[联系销售](https://stripe.com/contact/sales)。

Powered by [Markdoc](https://markdoc.dev)

注册来接收最新的开发人员资讯：

注册

您可以随时取消订阅。请阅读我们的[隐私政策](https://stripe.com/privacy)。

本页

[Customer consent](#customer-consent "Customer consent")

[Customer unsubscribe requests](#customer-unsubscribe-requests "Customer unsubscribe requests")

[Privacy policy update](#privacy-policy-update "Privacy policy update")

使用的产品

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

Stripe Shell 可提供最佳桌面体验。

    $

---

## URL: https://docs.stripe.com/payments/checkout/free-trials

 Configure free trials | Stripe Documentation     

[Skip to content](#main-content)

Configure free trials

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Ffree-trials)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Ffree-trials)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customise look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customisation depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information such as shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out")

[Manage your product catalogue](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

Configure free trials

[Limit customers to one subscription](/payments/checkout/limit-subscriptions)

[Set billing cycle date](/payments/checkout/billing-cycle)

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment Methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United Kingdom)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Subscriptions](/payments/subscriptions "Subscriptions")

Configure free trials
=====================

Delay payments on subscriptions using free trial periods.
---------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

You can configure a Checkout Session to start a customer’s subscription with a free trial by passing one of the following parameters:

*   [subscription\_data.trial\_period\_days](/api/checkout/sessions/create#create_checkout_session-subscription_data-trial_period_days), the length (in days) of your free trial.
*   [subscription\_data.trial\_end](/api/checkout/sessions/create#create_checkout_session-subscription_data-trial_end), a Unix timestamp representing the end of the trial period.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d mode=subscription \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "subscription_data[trial_period_days]"=30`

Free trials without collecting a payment method
-----------------------------------------------

By default, Checkout Sessions collect a payment method to use after the trial ends. You can sign customers up for free trials without collecting payment details by passing [payment\_method\_collection=if\_required](/api/checkout/sessions/create#create_checkout_session-payment_method_collection).

Choose whether to cancel or pause the subscription if the customer doesn’t provide a payment method before the trial ends by passing [trial\_settings.end\_behavior.missing\_payment\_method](/api/checkout/sessions/create#create_checkout_session-subscription_data-trial_settings-end_behavior-missing_payment_method).

*   **Cancel subscription**\-If the free trial subscription ends without a payment method, it cancels immediately. You can create another subscription if the customer decides to subscribe to a paid plan in the future.
*   **Pause subscription**\-If the free trial subscription ends without a payment method, it pauses and doesn’t cycle until it’s resumed. When a subscription is paused, it doesn’t generate invoices (unlike when a subscription’s [payment collection](/billing/subscriptions/pause-payment) is paused). When your customer adds their payment method after the subscription has paused, you can resume the same subscription. The subscription can remain paused indefinitely.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d mode=subscription \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "subscription_data[trial_period_days]"=30 \  -d "subscription_data[trial_settings][end_behavior][missing_payment_method]"=cancel \  -d payment_method_collection=if_required`

### Collect payment details automatically

Before the trial expires, collect payment details from your customer.

Under **Manage free trial messaging** in your [Subscriptions and emails settings](https://dashboard.stripe.com/settings/billing/automatic), you can choose to automatically send a reminder email when a customer’s trial is about to expire.

Next, select the **Link to a Stripe-hosted page** option so the reminder email contains a link for the customer to add or update their payment details. We don’t send free trial reminder emails in test mode. Learn more about how to [set up free trial reminders](/billing/revenue-recovery/customer-emails#trial-ending-reminders).

You must comply with card network requirements when offering trials. Learn more about [compliance requirements for trials and promotions](/billing/subscriptions/trials#compliance).

### Collect payment details in the Billing customer portal

You can also send the reminder email yourself, and redirect customers to the Billing customer portal to add their payment details.

First, configure the [Billing customer portal](/customer-management) to enable your customers to manage their subscriptions.

Next, collect billing information from your customers:

1.  Listen to the `customer.subscription.trial_will_end` [event](/api/events/types#event_types-customer.subscription.trial_will_end).
2.  If the subscription doesn’t have a [default payment method](/api/subscriptions/object#subscription_object-default_payment_method), get the customer’s email using the [Customers API](/api/customers/retrieve) and send them a message with a link to your site. It’s helpful to embed the customer ID in the email, for example `https://example.com?...&customer={{CUSTOMER_ID}}`.
3.  When the customer lands on your site, create a customer portal session using the customer ID from the previous step.
4.  [Redirect](/customer-management/integrate-customer-portal#redirect) the customer to the customer portal, where they can update their subscription with payment details.

Your customers can also [resume their paused subscription](/billing/subscriptions/trials#resume-a-paused-subscription) in the customer portal by selecting **Start subscription**, then adding a payment method. View [free trial periods](/billing/subscriptions/trials#create-free-trials-without-payment) to learn how to configure a subscription to pause or cancel when a free trial ends without a payment method attached.

Combining trials with usage-based billing
-----------------------------------------

You can use trial periods for subscriptions with [usage-based billing](/products-prices/pricing-models#usage-based-pricing). During the trial period, any usage accrued doesn’t count toward the total charged to the customer at the end of the billing cycle. After the trial period ends, usage accrues and is billed at the end of the next billing cycle.

### Trials and aggregate usage

If you use the `aggregate_usage` [parameter](/api/prices/create#create_price-recurring-aggregate_usage) and set the behavior to `last_ever`, your customer is billed for the last usage record if it falls within the trial period, even if the usage occurred during the trial period.

For example, if you provide file storage you might want to offer a month of free storage, but then charge for the first month if the customer continues to store files with your service.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access programme](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Free trials without collecting a payment method](#free-trials-without-payment-method "Free trials without collecting a payment method")

[Collect payment details automatically](#collect-payment "Collect payment details automatically")

[Collect payment details in the Billing customer portal](#collect-payment-details-in-the-billing-customer-portal "Collect payment details in the Billing customer portal")

[Combining trials with usage-based billing](#combining-trials-with-metered-prices "Combining trials with usage-based billing")

[Trials and aggregate usage](#trials-and-aggregate-usage "Trials and aggregate usage")

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/migrating-prices

 Checkout prices migration guide | Stripe Documentation     

[Skip to content](#main-content)

Build a checkout page

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigrating-prices)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigrating-prices)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customise look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customisation depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information such as shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out")

[Manage your product catalogue](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

Migrate Checkout to use Prices

Build an advanced integration

Build an in-app integration

Payment Methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United Kingdom

English (United Kingdom)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

Checkout prices migration guide
===============================

Learn how to update your integration to use prices with Stripe Checkout.
------------------------------------------------------------------------

The [Prices API](/api/prices) adds new features and flexibility to how you charge customers. This new integration offers:

*   More unified modeling for Checkout items—instead of plans, [SKUs](/api/skus "SKU"), and inline line items, every item is now a _price_.
*   The ability to render product images for recurring items.
*   Create a reusable product and price catalogue instead of one-off line items.
*   Create inline pricing for [subscriptions](/billing/subscriptions/creating "subscriptions").
*   Apply dynamic tax rates to [subscriptions](/billing/taxes/collect-taxes?tax-calculation=tax-rates#adding-tax-rates-to-checkout) and [one-off payments](/payments/checkout/taxes).

Don’t want to migrate? You can continue to use your current integration, but new features aren’t supported. You can use any new plans or recurring prices you create in the `plan` parameter of your existing API calls.

Products and prices overview
----------------------------

[Prices](/api/prices "Prices") are a new, core entity within Stripe that works with subscriptions, [invoices](/api/invoices "invoices"), and Checkout. Each price is tied to a single [Product](/api/products "Products"), and each product can have multiple prices. Different physical goods or levels of service should be represented by products. Pricing of that product should be represented by prices.

Prices define the base price, currency, and—for recurring products—the billing cycle. This allows you to change and add prices without needing to change the details of what you offer. For example, you might have a single “gold” product that has prices for 10 USD/month, 100 USD/year, 9 EUR/month, and 90 EUR/year. Or you might have a blue t-shirt with 20 USD and 15 EUR prices.

One-time payments
-----------------

Integrations for one-off payments have the following changes:

*   Instead of ad-hoc line items (that is, setting the name, amount, and currency), creating a Checkout Session requires creating a [product](/api/products "Products") and, usually, a [price](/api/prices "Prices").
*   [mode](/api/checkout/sessions/create#create_checkout_session-mode) is now required.

The client-side code remains the same.

### Mapping table

Instead of defining each field on `line_items`, Checkout uses the underlying product and price objects to determine name, description, amount, currency, and images. You can [create products and prices](/payments/accept-a-payment) with the API or Dashboard.

Without prices

With prices

`line_items.name`

`product.name`

`line_items.description`

`product.description`

`line_items.amount`

*   `price.unit_amount`
*   `price_data.unit_amount` (if defined when the Checkout Session is created)

`line_items.currency`

*   `price.currency`
*   `price_data.currency` (if defined when the Checkout Session is created)

`line_items.images`

`product.images` (displays the first image supplied)

### Server-side code for inline items

Previously, you could only create one-off items inline. With prices, you can continue to configure your items inline, but you can also define your prices dynamically with [price\_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data) when you create the Checkout Session.

When you create the Checkout Session with `price_data`, reference an existing product ID with [price\_data.product](/api/checkout/sessions/create#create_checkout_session-line_items-price_data-product), or define your product details dynamically using [price\_data.product\_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data-product_data). The following example demonstrates the flow for creating a one-off item.

Command Line

Select a languagecurl

`curl https://api.stripe.com/v1/checkout/sessions \   -u sk_test_26PHem9AhJZvU623DfE1x4sd  : \   -d "line_items[0][quantity]"=1 \   -d "line_items[0][amount]"=2000 \   -d "line_items[0][name]"=T-shirt \   -d "line_items[0][description]"="Comfortable cotton t-shirt" \   -d "line_items[0][images][]"="[https://example.com/t-shirt.png](https://example.com/t-shirt.png)" \   -d "line_items[0][currency]"=usd \   -d "line_items[0][price_data][unit_amount]"=2000 \   -d "line_items[0][price_data][product_data][name]"=T-shirt \   -d "line_items[0][price_data][product_data][description]"="Comfortable cotton t-shirt" \   -d "line_items[0][price_data][product_data][images][]"="[https://example.com/t-shirt.png](https://example.com/t-shirt.png)" \   -d "line_items[0][price_data][currency]"=usd \   -d mode=payment \   -d success_url="[https://example.com/success](https://example.com/success)" \   -d cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

### Server-side code for one-time prices

With this new integration, you can [create a product and price catalogue](/payments/accept-a-payment) upfront instead of needing to define the amount, currency, and name each time you create a Checkout Session.

You can either create a product and price with the [Prices API](/api/prices) or through the [Dashboard](https://dashboard.stripe.com/products). You will need the price ID to create the Checkout Session. The following example demonstrates how to create a product and price through API:

Command Line

Select a languagecurl

`curl https://api.stripe.com/v1/products \   -u sk_test_26PHem9AhJZvU623DfE1x4sd  : \   -d name=T-shirt \   -d description="Comfortable cotton t-shirt" \   -d "images[]"="https://example.com/t-shirt.png" curl https://api.stripe.com/v1/prices \   -u sk_test_26PHem9AhJZvU623DfE1x4sd  : \   -d product="{{PRODUCT_ID}}" \   -d unit_amount=2000 \   -d currency=usd curl https://api.stripe.com/v1/checkout/sessions \   -u sk_test_26PHem9AhJZvU623DfE1x4sd  : \   -d "line_items[0][quantity]"=1 \   -d "line_items[0][amount]"=2000 \   -d "line_items[0][name]"=T-shirt \   -d "line_items[0][description]"="Comfortable cotton t-shirt" \   -d "line_items[0][images][]"="https://example.com/t-shirt.png" \   -d "line_items[0][currency]"=usd \   -d "line_items[0][price]"="{{PRICE_ID}}" \   -d mode=payment \   -d success_url="https://example.com/success" \   -d cancel_url="https://example.com/cancel"`

Subscriptions
-------------

Integrations for recurring payments have the following changes:

*   All items are passed into a single [line\_items](/api/checkout/sessions/create#create_checkout_session-line_items) field, instead of `subscription_data.items`.
*   [mode](/api/checkout/sessions/create#create_checkout_session-mode) is now required. Set `mode=subscription` if the session includes any recurring items.

The client-side code remains the same. Existing plans can be used wherever recurring prices are accepted.

### Server-side code with plans

Here is a before and after example of creating a Checkout Session with a trial and using an existing plan, which can be used interchangeably with a price. The plan is now passed into `line_items` instead of `subscription_data.items`.

Command Line

Select a languagecurl

`curl https://api.stripe.com/v1/checkout/sessions \   -u sk_test_26PHem9AhJZvU623DfE1x4sd  : \   -d "subscription_data[items][][plan]"="{{PRICE_OR_PLAN_ID}}" \   -d "line_items[0][price]"="{{PRICE_OR_PLAN_ID}}" \   -d "line_items[0][quantity]"=1 \   -d mode=subscription \   -d success_url="https://example.com/success" \   -d cancel_url="https://example.com/cancel"`

### Server-side code for recurring price with setup fee

If you have recurring plans with a one-off setup fee, create the product and price representing the one-off fee before creating the Checkout Session. See the [mapping table](#mapping-table-server-one-time) for how the old `line_items` fields map to the new integration. You can either create a product and price through the [Prices API](/api/prices) or through the [Stripe Dashboard](https://dashboard.stripe.com/products). You can also [create the one-off item inline](/payments/checkout/migrating-prices#server-side-code-for-inline-items). The following example uses an existing price ID:

Command Line

Select a languagecurl

`curl https://api.stripe.com/v1/checkout/sessions \   -u sk_test_26PHem9AhJZvU623DfE1x4sd  : \   -d "line_items[0][quantity]"=1 \   -d "line_items[0][amount]"=2000 \   -d "line_items[0][name]"=T-shirt \   -d "line_items[0][description]"="Comfortable cotton t-shirt" \   -d "line_items[0][images][]"="https://example.com/t-shirt.png" \   -d "line_items[0][currency]"=usd \   -d "subscription_data[items][][plan]"="{{PLAN_ID}}" \   -d "line_items[0][price]"="{{PRICE_OR_PLAN_ID}}" \   -d "line_items[0][quantity]"=1 \   -d "line_items[1][price]"="{{ONE_TIME_PRICE_ID}}" \   -d "line_items[1][quantity]"=1 \   -d mode=subscription \   -d success_url="https://example.com/success" \   -d cancel_url="https://example.com/cancel"`

Response object changes
-----------------------

Instead of listing items with `display_items`, the Checkout Session object uses `line_items`. The `line_items` field does not render by default as `display_items` did, but you can include it using [expand](/api/expanding_objects) when creating a Checkout Session:

Command Line

Select a languagecurl

`curl https://api.stripe.com/v1/checkout/sessions \   -u sk_test_26PHem9AhJZvU623DfE1x4sd  : \   -d "payment_method_types[]"="card" \   -d "mode"="payment" \   -d "line_items[0][price]"="{{PRICE_ID}}" \   -d "line_items[0][quantity]"=1 \   -d "success_url"="https://example.com/success" \   -d "cancel_url"="https://example.com/cancel" \   -d "expand[]"="line_items"`

Webhook changes
---------------

Since `line_items` is includable, the `checkout.session.completed` [webhook](/webhooks "webhook") response no longer list items by default. The smaller response object enables you to receive your Checkout webhooks faster. You can retrieve items with the new `line_items` endpoint:

Command Line

Select a languagecurl

`curl https://api.stripe.com/v1/checkout/sessions/{{CHECKOUT_SESSION_ID}}/line_items \   -u sk_test_26PHem9AhJZvU623DfE1x4sd  :`

For more details, see [fulfilling orders with Checkout](/checkout/fulfillment).

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access programme](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Products and prices overview](#product-price-overview "Products and prices overview")

[One-time payments](#one-time-payments-changes "One-time payments")

[Mapping table](#mapping-table-server-one-time "Mapping table")

[Server-side code for inline items](#server-side-code-for-inline-items "Server-side code for inline items")

[Server-side code for one-time prices](#server-one-time-prices "Server-side code for one-time prices")

[Subscriptions](#subscription-changes "Subscriptions")

[Server-side code with plans](#server-subscription-plans "Server-side code with plans")

[Server-side code for recurring price with setup fee](#server-side-code-for-recurring-price-with-setup-fee "Server-side code for recurring price with setup fee")

[Response object changes](#response-object-changes "Response object changes")

[Webhook changes](#webhook-changes "Webhook changes")

Products Used

[

Checkout





](/payments/checkout)

[

Billing





](/billing)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/customization/policies

 Customize text and policies | Stripe Documentation     

[Skip to content](#main-content)

Customise text and policies

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fpolicies)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fpolicies)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customise look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customisation depends on the product you use.")

[Customise the appearance](/payments/checkout/customization/appearance)

Customise text and policies

[Customise behaviour](/payments/checkout/customization/behavior)

[Use your custom domain](/payments/checkout/custom-domains)

[Collect additional information](/payments/checkout/collect-additional-info "Collect information such as shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out")

[Manage your product catalogue](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment Methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

India

English (United Kingdom)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Customize look and feel](/payments/checkout/customization "Customize look and feel")

Customize text and policies
===========================

Customize the text that your customers see, and the policies Checkout displays.
-------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Add custom text
---------------

You can present additional text to customers when they pay with Stripe Checkout, such as shipping and processing times.

#### Warning

You’re prohibited from using this feature to create custom text that violates or creates ambiguity with the Stripe generated text on Checkout, obligations under your Stripe agreement, Stripe’s policies, and applicable laws.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_tR3PYbcVNZZ796tH88S4VQ2u  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \  -d "shipping_address_collection[allowed_countries][0]"=US \   --data-urlencode "custom_text[shipping_address][message]"="Please note that we can't guarantee 2-day delivery for PO boxes at this time." \   --data-urlencode "custom_text[submit][message]"="We'll email you instructions on how to get started." \   --data-urlencode "custom_text[after_submit][message]"="Learn more about **your purchase** on our [product page]([https://www.stripe.com/).](https://www.stripe.com/))" \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

![Custom text near shipping address collection](https://b.stripecdn.com/docs-statics-srv/assets/shipping-address-custom-text.b0b578d66d2bd415d0b0fe03106d27df.png)

Custom text near the shipping address collection fields

![Custom text above the pay button](https://b.stripecdn.com/docs-statics-srv/assets/submit-custom-text.bf46135c06b7c33c1ce9c9b09e4206c9.png)

Custom text above the **Pay** button

![Custom text below the pay button](https://b.stripecdn.com/docs-statics-srv/assets/custom-text-after-submit.32dbd97008b3f189145bcd07c4562bb4.png)

Custom text after the **Pay** button

Your custom text can be up to 1200 characters in length. However, Stripe Checkout is optimized for conversion, and adding extra information might affect your conversion rate. You can bold text or insert a link using [Markdown syntax](https://www.markdownguide.org/cheat-sheet/).

Customize policies and contact information
------------------------------------------

You can display your return, refund, and legal policies, and your support contact information to your customers on Checkout. Go to [Checkout Settings](https://dashboard.stripe.com/settings/checkout) to configure the information you want to display, including:

*   Details about your return and refund policies
*   Your support phone number, email, and website
*   Links to your terms of service and privacy policy

Presenting this information can increase buyer confidence and minimize cart abandonment.

### Configure support and legal policies

From [Checkout Settings](https://dashboard.stripe.com/settings/checkout), add support contact information to your sessions by enabling **Contact information**. Similarly, add links to your **Terms of service** and **Privacy policy** to your sessions by enabling **Legal policies**. If you require customers to implicitly consent to your legal policies when they complete their checkout, select the **Display agreement to legal terms** checkbox.

You must add your support contact information and legal policy links in your [Public Detail Settings](https://dashboard.stripe.com/settings/public).

The following previews show how Checkout displays a dialog with the support contact information, links to the store legal policies, and information about the payment terms.

![A checkout page with contact information.](https://b.stripecdn.com/docs-statics-srv/assets/contact-modal.2b81bc2e74657f7c94a45a743439c81f.png)

Preview of contact information on Checkout.

![A checkout page with legal policies.](https://b.stripecdn.com/docs-statics-srv/assets/legal-modal.9351cb51408c2a9f5c0ae23aab03e138.png)

Preview of legal policies on Checkout.

### Configure return and refund policies

Display your return, refund, or exchange policies, by enabling **Return and Refund policies**. Although businesses that sell physical goods use return policies, businesses that sell digital goods or customized physical goods typically use refund policies. Because they’re not mutually exclusive, you can select both options if your business sells both categories of goods. You can edit your return and refund details, including:

*   Whether you accept returns, refunds, or exchanges
*   Whether returns, refunds, or exchanges are free or if they’re subject to a fee
*   How many days after a purchase you’ll accept returns, refunds, or exchanges
*   How customers can return items shipped to them
*   Whether you accept in-store returns
*   A link to the full return and refund policy
*   A custom message

If you accept free returns, refunds, or exchanges, Checkout highlights the policy for customers.

The following previews show how Checkout displays a return policy. In this example, it’s for purchases that can be returned by shipping them or in-store for a full refund (or exchange) for up to 60 days. You can display similar information for refunds.

![Preview of return policies on Checkout](https://b.stripecdn.com/docs-statics-srv/assets/return-policy-modal.0c7a9ff71b8bc2c155842532801e06a8.png)

Preview of return policies on Checkout.

![Preview of a policy highlight on Checkout](https://b.stripecdn.com/docs-statics-srv/assets/policy-highlight.334828420693a33d376977a2c0fe5851.png)

Preview of a policy highlight on Checkout.

### Collect a terms of service agreement

Businesses often require their customers to agree to their terms of service before they can pay. This might depend on the type of product or subscription. Checkout helps you collect the necessary agreement by requiring a customer to accept your terms before paying.

![Collect terms of service agreement](https://b.stripecdn.com/docs-statics-srv/assets/terms-of-service-consent-collection.dec90bde6d1a3c5d4c0b3e7b8e644a52.png)

Collect terms of service agreement

You can collect a terms of service agreement with Stripe Checkout when you create a Session:

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_tR3PYbcVNZZ796tH88S4VQ2u  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=2 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "consent_collection[terms_of_service]"=required \   --data-urlencode "custom_text[terms_of_service_acceptance][message]"="I agree to the [Terms of Service]([https://example.com/terms)](https://example.com/terms))"`

When `consent_collection.terms_of_service='required'`, Checkout dynamically displays a checkbox for collecting the customer’s terms of service agreement. If `consent_collection.terms_of_service='none'`, Checkout won’t display the checkbox and won’t require customers to accept the terms of service. Before requiring agreement to your terms, set your terms of service URL in your [public details](https://dashboard.stripe.com/settings/public) of your business. Setting a privacy policy URL is optional—Checkout also links to your privacy policy when a URL to your Privacy policy is set in your [public details](https://dashboard.stripe.com/settings/public).

After a customer completes checkout, you can verify that the customer accepted your terms of service by looking at the Session object in the `checkout.session.completed` webhook, or by retrieving the Session using the API. When the terms are accepted, the Session’s [consent.terms\_of\_service](/api/checkout/sessions/object#checkout_session_object-consent) field is set to `accepted`.

You can customize the text that appears next to the checkbox by using `custom_text.terms_of_service_acceptance`. You need to set `consent_collection.terms_of_service='required'`. To use your own terms, insert a Markdown link. For example: `I agree to the [Terms of Service](https://example.com/terms)`

#### Warning

Consult your legal and compliance advisors before making any changes to this text. You can’t use this feature to display custom text that violates or creates ambiguity with the Stripe-generated text on Checkout, obligations under your Stripe agreement, Stripe policies, and applicable laws.

### Collect consent for promotional emails

You can send promotional emails to inform customers of new products and to share coupons and discounts. Before doing so, you must [collect their consent](/payments/checkout/promotional-emails-consent) to receive promotional emails.

Customize payment method reuse agreement
----------------------------------------

Checkout displays a message to customers about reusing their payment method when a session is in either setup or subscription mode, or when a payment mode session has `setup_future_usage` set. You can hide this text and use custom text to set different language about the rules for reusing a payment method. This text appears alongside additional legal text for some payment methods, and includes information about trials when applicable.

![Default payment method reuse agreement display in subscription mode](https://b.stripecdn.com/docs-statics-srv/assets/default-subscription-mode-payment-method-reuse-agreement.caee311155d9948637a53aafded801af.png)

Default payment method reuse agreement in subscription mode

#### Warning

By customizing this text, you’re responsible for maintaining compliance, which includes updating this text as card network rules and local regulations change. Don’t use this feature without consulting with your legal team or setting custom text that includes information regarding the reuse of the payment method. Make sure that your customized text covers all modes you plan to support.

To hide the payment method reuse agreement text, set `consent_collections.payment_method_reuse_agreement.position='hidden'`. Checkout won’t display its default language governing the reuse of the payment method. To set your own text in place of Stripe’s default language, set `custom_text.after_submit.message`. You can also use `custom_text.submit` or `custom_text.terms_of_service_acceptance` to display your own version of this language.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_tR3PYbcVNZZ796tH88S4VQ2u  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=subscription \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "consent_collection[payment_method_reuse_agreement][position]"=hidden \   --data-urlencode "custom_text[after_submit][message]"="You can cancel your subscription at any time by [logging into your account]([https://www.example.com/)](https://www.example.com/))"`

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access programme](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Add custom text](#add-custom-text "Add custom text")

[Customize policies and contact information](#policies "Customize policies and contact information")

[Configure support and legal policies](#configure-support-and-legal-policies "Configure support and legal policies")

[Configure return and refund policies](#configure-return-and-refund-policies "Configure return and refund policies")

[Collect a terms of service agreement](#collect-a-terms-of-service-agreement "Collect a terms of service agreement")

[Collect consent for promotional emails](#collect-consent-for-promotional-emails "Collect consent for promotional emails")

[Customize payment method reuse agreement](#customize-payment-method-reuse-agreement "Customize payment method reuse agreement")

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/promotional-emails-consent

 Collect consent for promotional emails | Stripe 文档     

[调至内容部分](#main-content)

收集促销邮件通知许可

[

创建账户



](https://dashboard.stripe.com/register)或[

登录



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpromotional-emails-consent)

[

](/)

搜索文档

/

[创建账户](https://dashboard.stripe.com/register)

[

登录



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpromotional-emails-consent)

[

开始



](/get-started)

[

付款



](/payments)

[

财务自动化



](/finance-automation)

[

平台和交易市场



](/connect)

[

银行即服务



](/financial-services)

[

开发人员工具



](/development)

[

开始



](/get-started)

[

付款



](/payments)

[

财务自动化



](/finance-automation)

[

开始



](/get-started)

[

付款



](/payments)

[

财务自动化



](/finance-automation)

[

平台和交易市场



](/connect)

[

银行即服务



](/financial-services)

API 和 SDK

帮助

[概览](/payments)

关于 Stripe 支付

[升级您的集成应用](/payments/upgrades "改进现有集成")

支付分析

线上付款

[概览](/payments/online-payments "了解在线收款的集成选项。")[查找您的用例](/payments/use-cases/get-started "了解 Stripe 如何能支持您的业务。")

Use Payment Links

构建结账页面

[概览](/payments/checkout/build-integration "用 Checkout 构建支付体验。")

[快速开始](/payments/checkout/quickstarts "使用实例代码开始。")

[自定义外观样式](/payments/checkout/customization "控制结账页面的外观。自定义级别取决于您使用的产品。")

[收集额外信息](/payments/checkout/collect-additional-info "在结账过程中收集客户的收货地址和电话号码等信息。")

[收集物理地址](/payments/collect-addresses "了解如何收集账单地址和收货地址。")

[收取运费](/payments/during-payment/charge-shipping)

[收集电话号码](/payments/checkout/phone-numbers "使用 Checkout 收集客户的电话号码")

[添加自定义字段](/payments/checkout/custom-fields)

收集促销邮件通知许可

[合规促销邮件](/payments/checkout/compliant-promotional-emails)

[收税](/payments/checkout/taxes)

[动态更新结账流程](/payments/checkout/dynamic-updates "在客户结账过程中进行更新")

[管理产品目录](/payments/checkout/product-catalog)

[订阅](/payments/subscriptions "用 Checkout 管理订阅")

[管理支付方式](/payments/checkout/payment-methods)

[让客户用本地货币支付](/payments/checkout/adaptive-pricing)

[添加折扣、追加销售和交叉销售](/payments/checkout/promotions)

[设置未来付款](/payments/checkout/save-and-reuse "了解如何保存支付详情并在将来对客户扣款")

[支付过程中保存付款详情](/payments/checkout/save-during-payment "支付过程中保存付款详情")

[付款后](/payments/checkout/after-the-payment)

[具有 Checkout Sessions API 更改日志的 Element](/checkout/elements-with-checkout-sessions-api/changelog)

[从传统 Checkout 迁移](/payments/checkout/migration)

[迁移 Checkout 来使用 Prices](/payments/checkout/migrating-prices)

构建高级集成应用

构建应用内集成

支付方式

添加支付方式

管理支付方式

用 Link 更快结账

支付 UI

Payment Link

结账

Web Elements

应用内 Element

支付场景

自定义支付流程

灵活收单

线下支付

Terminal

其他 Stripe 产品

Financial Connections

加密货币

Climate

提现链接

美国

简体中文

[首页](/ "首页")[付款](/payments "付款")Build a checkout page[Collect additional information](/payments/checkout/collect-additional-info "Collect additional information")

Collect consent for promotional emailsUS only
=============================================

Learn how to collect permission from customers so that you can send them promotional emails.
--------------------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Promotional emails are often sent to inform customers of new products and to share coupons and discounts. For example, you can use them to subscribe customers to company newsletters or [send cart abandonment emails](/payments/checkout/abandoned-carts).

![Collect consent for promotional emails](https://b.stripecdn.com/docs-statics-srv/assets/promotional-consent-collection.444ead1668bd41537b9a07b2dbdc219a.png)

Collect consent from customers to send them promotional emails

To protect consumers from unwanted spam, customers must agree to receiving promotional emails before you can contact them. Checkout helps you collect the necessary consent, where applicable, to send promotional emails. Learn more about [promotional email requirements](/payments/checkout/compliant-promotional-emails).

[

Collect consent


-----------------





](#collect-consent)

You can collect promotional email consent with Stripe Checkout when you create the session:

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=2 \  -d customer=  {{CUSTOMER_ID}}   \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "consent_collection[promotions]"=auto`

When `consent_collection.promotions='auto'`, Checkout dynamically displays a checkbox for collecting the customer’s consent to promotional content.

#### 备注

When the checkbox is shown, the default state depends on the customer’s country and the country your business is based in. Data privacy laws vary by jurisdiction, so Checkout disables or limits this feature when local regulations prohibit it.

[

Store consent and email address


---------------------------------





](#store-consent)

The Checkout Session’s [consent](/api/checkout/sessions/object#checkout_session_object-consent) attribute records whether or not the session collected promotional consent from the customer.

As customers complete purchases, keep track of which customers consent to promotional content. You can create or update an existing [webhook](/webhooks "Webhook") handler to do this. Listen to the `checkout.session.completed` event, check for the `consent.promotions` status, and then store email addresses for customers who give consent.

Node

``// Find your endpoint's secret in your Dashboard's webhook settings const endpointSecret = 'whsec_...';  // Using Express const app = require('express')();  // Use body-parser to retrieve the raw body as a buffer const bodyParser = require('body-parser');  const recordPromotionalEmailConsent = (email, promoConsent) => {   // TODO: fill me in   console.log("Recording promotional email consent", email, promoConsent); }  app.post('/webhook', bodyParser.raw({type: 'application/json'}), (request, response) => {   const payload = request.body;   const sig = request.headers['stripe-signature'];    let event;    try {     event = stripe.webhooks.constructEvent(payload, sig, endpointSecret);   } catch (err) {     return response.status(400).send(`Webhook Error: ${err.message}`);   }    // Handle the checkout.session.completed event   if (event.type === 'checkout.session.completed') {     const session = event.data.object;     const promoConsent = session.consent?.promotions;     const email = session.customer_details.email;      // Record whether or not the customer has agreed to receive promotional emails     recordPromotionalEmailConsent(email, promoConsent)      // Handle order fulfillment   }   response.status(200).end(); });``

After you’ve configured Checkout to collect consent for sending customers promotional content, you can [recover abandoned carts](/payments/checkout/abandoned-carts) by following up with leads for customers that left the checkout flow before completing payment.

此页面的内容有帮助吗？

是否

需要帮助？[联系支持](https://support.stripe.com/)。

加入我们的[早期使用计划](https://insiders.stripe.dev/)。

查看我们的[产品更改日志](https://stripe.com/blog/changelog)。

有问题？[联系销售](https://stripe.com/contact/sales)。

Powered by [Markdoc](https://markdoc.dev)

注册来接收最新的开发人员资讯：

注册

您可以随时取消订阅。请阅读我们的[隐私政策](https://stripe.com/privacy)。

本页

[Collect consent](#collect-consent "Collect consent")

[Store consent and email address](#store-consent "Store consent and email address")

使用的产品

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

Stripe Shell 可提供最佳桌面体验。

    $

---

## URL: https://docs.stripe.com/payments/checkout/discounts?oo-step=true&should-crawl=true&record-id=9863fcki9r&wait-before-scraping=2000&save-html=true&save-markdown=true

 Add discounts | Stripe Documentation     

[Skip to content](#main-content)

Add discounts

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fdiscounts)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fdiscounts)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross\-sells](/payments/checkout/promotions)

Add discounts

[Configure subscription upsells](/payments/checkout/upsells)

[Configure cross\-sells](/payments/checkout/cross-sells)

[Let customers complete orders for free](/payments/checkout/no-cost-orders)

[Display yearly prices in monthly terms](/payments/checkout/yearly-price-display)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in\-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In\-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In\-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Australia

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Add discounts, upsells, and cross\-sells](/payments/checkout/promotions "Add discounts, upsells, and cross-sells")

Add discounts
=============

Reduce the amount charged to a customer by discounting their subtotal with coupons and promotion codes.
-------------------------------------------------------------------------------------------------------

Stripe\-hosted page

Embedded form

Embedded components

Public preview

You can use discounts to reduce the amount charged to a customer. Coupons and promotion codes allow you to:

*   Apply a discount to an entire purchase subtotal
*   Apply a discount to specific products
*   Reduce the total charged by a percentage or a flat amount
*   Create customer\-facing promotion codes on top of coupons to share directly with customers

#### Note

To use coupons for discounting [subscriptions](/billing/subscriptions/creating "subscriptions") with Checkout and Billing, see [Discounts for subscriptions](/billing/subscriptions/coupons).

Create a coupon
---------------

Coupons specify a fixed value discount. You can create customer\-facing promotion codes that map to a single underlying coupon. This means that the codes `FALLPROMO` and `SPRINGPROMO` can both point to one 25% off coupon. You can create coupons in the [Dashboard](https://dashboard.stripe.com/coupons) or with the [API](/api#coupons):

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/coupons \  -u "  sk_test_wsFx86XDJWwmE4dMskBgJYrt  :" \  -d percent_off=20 \  -d duration=once`

Use a coupon
------------

To create a session with an applied discount, pass the [coupon ID](/api/coupons/object#coupon_object-id) in the `coupon` parameter of the [discounts](/api/checkout/sessions/create#create_checkout_session-discounts) array. Checkout currently supports up to one coupon or promotion code.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_wsFx86XDJWwmE4dMskBgJYrt  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "discounts[0][coupon]"=  {{COUPON_ID}}   \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

Configure a coupon
------------------

Coupons have the following parameters that you can use:

*   `currency`
*   `percent_off` or `amount_off`
*   `max_redemptions`
*   `redeem_by`, the latest date customers can apply the coupon
*   `applies_to`, limits the products that the coupon applies to

#### Note

The coupon object adds discounts to both one\-time payments and subscriptions. Some coupon object parameters, like `duration`, only apply to [subscriptions](/billing/subscriptions/coupons).

### Limit redemption usage

The `max_redemptions` and `redeem_by` values apply to the coupon across every application. For example, you can restrict a coupon to the first 50 usages of it, or you can make a coupon expire by a certain date.

### Limit eligible products

You can limit the products that are eligible for discounts using a coupon by adding the product IDs to the `applies_to` hash in the Coupon object. Any promotion codes that map to this coupon only apply to the list of eligible products.

### Delete a coupon

You can delete coupons in the Dashboard or the API. Deleting a coupon prevents it from being applied to future transactions or customers.

Create a promotion code
-----------------------

Promotion codes are customer\-facing codes created on top of coupons. You can also specify additional restrictions that control when a customer can apply the promotion. You can share these codes with customers who can enter them during checkout to apply a discount.

To create a [promotion code](/api/promotion_codes), specify an existing `coupon` and any restrictions (for example, limiting it to a specific `customer`). If you have a specific code to give to your customer (for example, `FALL25OFF`), set the `code`. If you leave this field blank, we’ll generate a random `code` for you.

The `code` is case\-insensitive and unique across active promotion codes for any customer. For example:

*   You can create multiple customer\-restricted promotion codes with the same `code`, but you can’t reuse that `code` for a promotion code redeemable by any customer.
*   If you create a promotion code that is redeemable by any customer, you can’t create another active promotion code with the same `code`.
*   You can create a promotion code with `code: NEWUSER`, inactivate it by passing `active: false`, and then create a new promotion code with `code: NEWUSER`.

Promotion codes can be created in the coupons section of the [Dashboard](https://dashboard.stripe.com/coupons/create) or with the [API](/api#promotion_codes):

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/promotion_codes \  -u "  sk_test_wsFx86XDJWwmE4dMskBgJYrt  :" \  -d coupon={{COUPON_ID}} \   -d code=VIPCODE`

Use a promotion code
--------------------

Enable customer\-redeemable promotion codes using the [allow\_promotion\_codes](/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes) parameter in a Checkout Session. This enables a field in Checkout to allow customers to input promotion codes.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_wsFx86XDJWwmE4dMskBgJYrt  :" \  -d "line_items[0][price_data][unit_amount]"=2000 \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][quantity]"=1 \  -d mode=payment \  -d allow_promotion_codes=true \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)"`

Configure a promotion code
--------------------------

For each promotion code, you can customize eligible customers, redemptions, and other limits.

### Limit by customer

To limit a promotion to a particular customer, specify a [customer](/api/promotion_codes/create#create_promotion_code-customer) when creating the promotion code. If no customer is specified, any customer can redeem the code.

### Limit by first\-time order

You can also limit the promotion code to first\-time customers with [restrictions.first\_time\_transaction](/api/promotion_codes/create#create_promotion_code-restrictions-first_time_transaction). If the `customer` isn’t defined, or if a defined `customer` has no prior payments or non\-void [invoices](/api/invoices "invoices"), it’s considered a first\-time transaction.

#### Note

Sessions that don’t create [Customers](/api/customers) instead create [Guest Customers](https://support.stripe.com/questions/guest-customer-faq) in the Dashboard. Promotion codes limited to first\-time customers are still accepted for these Sessions.

### Set a minimum amount

With promotion codes, you can set a minimum transaction amount for eligible discount by configuring [minimum\_amount](/api/promotion_codes/create#create_promotion_code-restrictions-minimum_amount) and [minimum\_amount\_currency](/api/promotion_codes/create#create_promotion_code-restrictions-minimum_amount_currency). Since promotion code restrictions are checked at redemption time, the minimum transaction amount only applies to the initial payment for a subscription.

### Customize expirations

You can set an expiration date on the promotion code using [expires\_at](/api/promotion_codes/create#create_promotion_code-expires_at). If the underlying coupon already has `redeem_by` set, then the expiration date for the promotion code can’t be later than that of the coupon. If `promotion_code[expires_at]` isn’t specified, the coupon’s `redeem_by` automatically populates `expires_at`.

For example, you might have plans to support a coupon for a year, but you only want it to be redeemable for one week after a customer receives it. You can set `coupon[redeem_by]` to one year from now, and set each `promotion_code[expires_at]` to one week after it’s created.

### Limit redemptions

You can limit the number of redemptions by using [max\_redemptions](/api/promotion_codes/create#create_promotion_code-max_redemptions), which works similarly to the coupon parameter. If the underlying coupon already has `max_redemptions` set, then the `max_redemptions` for the promotion code can’t be greater than that of the coupon.

For example, you might want a seasonal sale coupon to be redeemable by the first 50 customers, but the winter promotion can only use 20 of those redemptions. In this scenario, you can set `coupon[max_redemptions]: 50` and `promotion_code[max_redemptions]: 20`.

### Inactive promotions

You can set whether a promotion code is currently redeemable by using the [active](/api/promotion_codes/create#create_promotion_code-active) parameter. However, if the underlying coupon for a promotion code becomes invalid, all of its promotion codes become permanently inactive. Similarly, if a promotion code reaches its `max_redemptions` or `expires_at`, it becomes permanently inactive. You can’t reactivate these promotion codes.

### Delete promotions

You can delete promotions in the Dashboard or the API. Deleting a promotion prevents it from being applied to future transactions or customers.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Create a coupon](#create-a-coupon "Create a coupon")

[Use a coupon](#use-a-coupon "Use a coupon")

[Configure a coupon](#configure-a-coupon "Configure a coupon")

[Limit redemption usage](#limit-redemption-usage "Limit redemption usage")

[Limit eligible products](#limit-eligible-products "Limit eligible products")

[Delete a coupon](#delete-a-coupon "Delete a coupon")

[Create a promotion code](#create-a-promotion-code "Create a promotion code")

[Use a promotion code](#use-promotion-code "Use a promotion code")

[Configure a promotion code](#configure-a-promotion-code "Configure a promotion code")

[Limit by customer](#limit-by-customer "Limit by customer")

[Limit by first\-time order](#limit-by-first-time-order "Limit by first-time order")

[Set a minimum amount](#set-a-minimum-amount "Set a minimum amount")

[Customize expirations](#customize-expirations "Customize expirations")

[Limit redemptions](#limit-redemptions "Limit redemptions")

[Inactive promotions](#inactive-promotions "Inactive promotions")

[Delete promotions](#delete-promotions "Delete promotions")

Products Used

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/manual-currency-prices?oo-step=true&should-crawl=true&record-id=hn4e4hp6yb&wait-before-scraping=2000&save-html=true&save-markdown=true

 Manual currency prices | Stripe Documentation     

[Skip to content](#main-content)

Define manual currency prices

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmanual-currency-prices)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmanual-currency-prices)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

Define manual currency prices

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Italy

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Let customers pay in their local currency](/payments/checkout/adaptive-pricing "Let customers pay in their local currency")

Manual currency prices
======================

Present local currencies to customers with manual currency prices.
------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Stripe supports manually defining prices in different currencies when creating [products](/products-prices/overview#get-started). However, Stripe recommends leveraging [Adaptive Pricing](/payments/checkout/adaptive-pricing) instead of manual currency prices to reduce currency exchange rate fluctuation risk and to automatically enable support for 50+ local currencies.

Use manual currency prices over Adaptive Pricing when:

*   Adaptive Pricing isn’t yet [supported](/payments/checkout/adaptive-pricing#restrictions) for your business or Checkout configuration (reach out to [adaptive-pricing-beta@stripe.com](mailto:adaptive-pricing-beta@stripe.com) to inquire about the preview).
*   You’re supporting a region where you’re comfortable taking on fluctuations in the currency’s exchange rate.

Manually defined multi-currency prices override Adaptive Pricing for those currencies, even if it’s enabled.

[

Create a multi-currency price

Dashboard

Server-side




---------------------------------------------------------





](#add-multiple-currencies-to-a-price)

Dashboard

API

1.  Navigate to a product in the [Dashboard](https://dashboard.stripe.com/products?active=true).
2.  Click **+Add another price** to create a new price.
3.  Fill in the price and select a currency. This first currency is the price’s default currency. Make sure all of your prices have the same default currency.
4.  Click **+Add a price by currency** to search and select from supported currencies, adding them to your price.
5.  Use the multi-currency price you created by passing its ID into [line items](/api/checkout/sessions/create#create_checkout_session-line_items-price) when you create a Checkout Session.

[

Create a Checkout Session

Server-side




------------------------------------------





](#create-checkout-session)

Create a Checkout Session using the multi-currency price:

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

[

Testing

Server-side

Client-side




-------------------------------------





](#testing)

To test local currency presentment for Checkout, Payment Links, and the [pricing table](/payments/checkout/pricing-table), pass in a location-formatted customer email that includes a suffix in a `+location_XX` format in the local part of the email. `XX` must be a valid [two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm).

For example, to test currency presentment for a customer in France, pass in an email such as `test+location_FR@example.com`.

When you visit the URL for a Checkout Session, Payment Link, or pricing table created with a location-formatted email, you see the same currency as a customer does in the specified country.

### Testing Checkout

When you create a Checkout Session, pass the location-formatted email as [customer\_email](/api/checkout/sessions/object#checkout_session_object-customer_email) to simulate Checkout from a particular country.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u   sk_test_9W1R4v0cz6AtC9PVwHFzywti  : \   -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \  -d success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode customer_email="test+location_FR@example.com"`

You can also create a [Customer](/api/customers/create) and specify their email that contains the `+location_XX` suffix. Stripe test cards work as usual.

When it’s possible to present the customer’s local currency in Checkout, the [Checkout Session](/api/checkout/sessions/object) object changes. Fields like `currency`, `payment_method_types`, and `amount_total` reflect the local currency and price.

### Testing Payment Links

For Payment Links, pass the location-formatted email as the `prefilled_email` [URL parameter](/payment-links/customize#customize-checkout-with-url-parameters) to test currency presentment for customers in different countries.

### Testing Pricing table

For the pricing table, pass the location-formatted email as the [customer-email](/payments/checkout/pricing-table#customer-email) attribute to test currency presentment for customers in different countries.

[

OptionalSpecify a currency

Server-side




-------------------------------------------





](#specify-currency)

Local payment methods
---------------------

The Checkout Session presents customers with popular payment methods compatible with their local currencies. For example, for customers located in the Netherlands, the Checkout Session converts prices to EUR and also present popular Dutch payment methods like iDEAL.

You can configure which payment methods you accept in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

Pricing tables
--------------

Manual currency prices also work with [pricing tables](/payments/checkout/pricing-table). To render local currencies to customers viewing your pricing table, all of the pricing table’s Prices must include the customer’s local currency in their `currency_options`. They must also include a `tax_behavior` for the given currency if you’re using Stripe Tax.

Supported integrations
----------------------

Checkout automatically presents the local currency to customers if all of the following are true:

*   The Checkout Session’s prices, shipping rates, and discounts have the relevant currency in their `currency_options`.
*   If a price on the Checkout Session has an upsell, the upsell’s price has the relevant currency in its `currency_options`.
*   For a Checkout Session using Stripe Tax, the `tax_behavior` on the Checkout Session is specified for the relevant currency for all of the Checkout Session’s prices, shipping rates, and discounts.
*   You didn’t specify a currency during Checkout Session creation.

If Checkout can’t localize the currency because the relevant currency option or `tax_behavior` is missing, the Session presents to the customer in the default currency. The default currency must be the same across all prices, shipping rates, and discounts.

### Restrictions

Price localization isn’t available for Checkout Sessions that:

*   Use manual tax rates.
*   Use `payment_intent_data.application_fee_amount` or `payment_intent_data.transfer_data.amount`.

Fees
----

Stripe’s standard transaction fees apply to automatically converted transactions:

*   Cards or payment methods fee
*   International cards or payment methods fee (if applicable)
*   Currency conversion fee

See the [pricing page](https://stripe.com/pricing) for more details about these fees.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Create a multi-currency price](#add-multiple-currencies-to-a-price "Create a multi-currency price")

[Create a Checkout Session](#create-checkout-session "Create a Checkout Session")

[Testing](#testing "Testing")

[Testing Checkout](#testing-checkout "Testing Checkout")

[Testing Payment Links](#testing-payment-links "Testing Payment Links")

[Testing Pricing table](#testing-pricing-table "Testing Pricing table")

[Local payment methods](#local-payment-methods "Local payment methods")

[Pricing tables](#pricing-table "Pricing tables")

[Supported integrations](#supported-integrations "Supported integrations")

[Restrictions](#restrictions "Restrictions")

[Fees](#fees "Fees")

Products Used

[

Checkout





](/payments/checkout)

[

Payment Links





](/payments/payment-links)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/yearly-price-display

 Display yearly prices in monthly terms | Documentación de Stripe     

[Ir a contenido](#main-content)

Mostrar precios anuales en términos mensuales

[

Crea una cuenta



](https://dashboard.stripe.com/register)o[

inicia sesión



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fyearly-price-display)

[

](/)

Busca en la documentación

/

[Crear cuenta](https://dashboard.stripe.com/register)

[

Iniciar sesión



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fyearly-price-display)

[

Empezar



](/get-started)

[

Pagos



](/payments)

[

Automatización de finanzas



](/finance-automation)

[

Plataformas y marketplaces



](/connect)

[

Banca como servicio



](/financial-services)

[

Herramientas para desarrolladores



](/development)

[

Empezar



](/get-started)

[

Pagos



](/payments)

[

Automatización de finanzas



](/finance-automation)

[

Empezar



](/get-started)

[

Pagos



](/payments)

[

Automatización de finanzas



](/finance-automation)

[

Plataformas y marketplaces



](/connect)

[

Banca como servicio



](/financial-services)

API y SDK

Ayuda

[Resumen](/payments)

Acerca de Stripe Payments

[Actualiza tu integración](/payments/upgrades "Mejora tu integración actual")

Análisis de pagos

Pagos por Internet

[Resumen](/payments/online-payments "Obtén información sobre las opciones de integración para aceptar pagos por Internet.")[Encuentra tu caso de uso](/payments/use-cases/get-started "Descubre cómo Stripe puede ayudar a tu empresa.")

Use Payment Links

Crear una página del proceso de compra

[Resumen](/payments/checkout/build-integration "Crea una experiencia de pagos con Checkout.")

[Guías de inicio rápido](/payments/checkout/quickstarts "Empieza con el código de muestra.")

[Personaliza el estilo](/payments/checkout/customization "Modifica la apariencia de tu página del proceso de compra. El nivel de personalización depende del producto que utilices.")

[Recolecta información adicional](/payments/checkout/collect-additional-info "Recolecta información como las direcciones de envío y los números de teléfono como parte del proceso de compra.")

[Cobrar impuestos](/payments/checkout/taxes)

[Actualiza forma dinámica el proceso de compra](/payments/checkout/dynamic-updates "Haz actualizaciones mientras tu cliente efectúa una compra.")

[Gestiona tu catálogo de productos](/payments/checkout/product-catalog)

[Suscripciones](/payments/subscriptions "Gestiona suscripciones con Checkout")

[Gestiona los métodos de pago](/payments/checkout/payment-methods)

[Permite que los clientes paguen en su divisa local](/payments/checkout/adaptive-pricing)

[Añade descuentos y ventas adicionales y cruzadas](/payments/checkout/promotions)

[Añadir descuentos](/payments/checkout/discounts)

[Configurar las ventas de productos de más valor de suscripciones](/payments/checkout/upsells)

[Configurar ventas cruzadas](/payments/checkout/cross-sells)

[Deja que los clientes completen pedidos de forma gratuita](/payments/checkout/no-cost-orders)

Mostrar precios anuales en términos mensuales

[Configurar pagos futuros](/payments/checkout/save-and-reuse "Descubre cómo guardar los datos de pago para cobrarles a tus clientes más tarde")

[Guardar datos de pago durante el pago](/payments/checkout/save-during-payment "Guardar datos de pago durante el pago")

[Después del pago](/payments/checkout/after-the-payment)

[Elements con el registro de cambios de la API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrar desde Checkout heredado](/payments/checkout/migration)

[Migrar Checkout para usar precios](/payments/checkout/migrating-prices)

Desarrolla una integración avanzada

Desarrolla una integración en la aplicación

Métodos de pago

Añadir métodos de pago

Gestiona los métodos de pago

Proceso de compra más rápido con Link

Interfaces de usuario de pagos

Payment Links

Checkout

Elements para la web

Elements en la aplicación

Escenarios de pago

Flujos de pagos personalizados

Capacidad adquirente flexible

Pagos en persona

Terminal

Otros productos de Stripe

Financial Connections

Criptomonedas

Climate

Enlaces de transferencia

Dinamarca

Español (España)

[Inicio](/ "Inicio")[Pagos](/payments "Pagos")Build a checkout page[Add discounts, upsells, and cross-sells](/payments/checkout/promotions "Add discounts, upsells, and cross-sells")

Display yearly prices in monthly terms
======================================

Help customers compare prices by displaying yearly prices in monthly terms.
---------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

You can display annually billed prices as their per month cost equivalent across Checkout, Payment Links, [pricing tables](/payments/checkout/pricing-table), and [buy buttons](/payment-links/buy-button). You can manage pricing display in your [Checkout and Payment Links settings](https://dashboard.stripe.com/settings/checkout).

Checkout and Payment Links
--------------------------

When you have pricing set to display `per month`, Checkout shows a label with the equivalent monthly rate below the yearly total. If the yearly price is an [upsell](/payments/checkout/upsells) from a monthly price and has a lower equivalent monthly rate, the old price displays with a strikethrough.

![A yearly recurring price with a monthly terms description in Checkout](https://b.stripecdn.com/docs-statics-srv/assets/checkout-with-upsell.7a3032232b5d4e1905c0f7ced7101ade.png)

Pricing table
-------------

When you have pricing set to display `per month`, the pricing table displays the equivalent monthly rate of eligible yearly prices followed by the total annual amount.

![A pricing table with yearly prices displayed in monthly terms](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table.a1b0b5b830c1ec8233dfc25733947f57.png)

Buy button
----------

When you have pricing set to display `per month`, the buy button displays the equivalent monthly rate of eligible yearly prices followed by the total annual amount.

![A buy button with a yearly price displayed in monthly terms](https://b.stripecdn.com/docs-statics-srv/assets/buy-button.a7a65d2d935600d581e4885a90585570.png)

Restrictions
------------

Customers, sessions, and pricing tables with any of the following features aren’t eligible to display `per month`:

*   A combination of recurring and one-time prices
*   Prices with recurring intervals that aren’t billed annually
*   Prices with free trials or [billing cycle anchors](/payments/checkout/billing-cycle)
*   [Usage-based pricing](/products-prices/pricing-models#usage-based-pricing)

¿Te ha sido útil la página?

SíNo

¿Necesitas ayuda? [Ponte en contacto con el equipo de soporte](https://support.stripe.com/).

Únete a nuestro [programa de acceso anticipado](https://insiders.stripe.dev/).

Consulta nuestro [registro de cambios de productos](https://stripe.com/blog/changelog).

¿Tienes alguna pregunta? [Ponte en contacto con el equipo de ventas](https://stripe.com/contact/sales).

Con tecnología de [Markdoc](https://markdoc.dev)

Inscríbete para recibir las actualizaciones para desarrolladores:

Inscríbete

Puedes cancelar la suscripción en cualquier momento. Consulta nuestra [Política de privacidad](https://stripe.com/privacy).

En esta página

[Checkout and Payment Links](#checkout-and-payment-links "Checkout and Payment Links")

[Pricing table](#pricing-table "Pricing table")

[Buy button](#buy-button "Buy button")

[Restrictions](#restrictions "Restrictions")

Productos utilizados

[

Checkout





](/payments/checkout)

[

Payment Links





](/payments/payment-links)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La experiencia con Stripe Shell es mejor en ordenadores de sobremesa.

    $

---

## URL: https://docs.stripe.com/payments/checkout/guest-customers?oo-step=true&should-crawl=true&record-id=76rqgvsl0z&wait-before-scraping=2000&save-html=true&save-markdown=true

 Guest customers | Stripe Documentation     

[Skip to content](#main-content)

Guest customers

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fguest-customers)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fguest-customers)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

Guest customers

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

Guest customers
===============

Learn how to track the activity of guest customers.
---------------------------------------------------

The [Customer object](/api/customers) represents a customer of your business, and it helps tracking subscriptions and payments that belong to the same customer. Checkout Sessions that don’t create Customers are associated with guest customers instead. Stripe automatically groups [guest customers in the Dashboard](https://dashboard.stripe.com/customers?type=guest) based on them having used the same card, email, or phone to make payments. This unified view helps you review purchasing behavior, refunds, chargebacks, or fraud.

Checkout supports passing in a [customer](/api/checkout/sessions/create#create_checkout_session-customer) to enable you to [prefill customer information](/payments/existing-customers?platform=web&ui=stripe-hosted) on the Checkout page and to associate the payment or subscription with a specific customer.

If you don’t pass in a `customer`, you can set [customer\_creation](/api/checkout/sessions/create#create_checkout_session-customer_creation) to configure whether or not Checkout automatically creates a Customer object when the session is confirmed.

Managing and monitoring guest customers
---------------------------------------

Even though you can’t manage or monitor guest customers in the same way as with Checkout Sessions that create Customers, you can still manage them and monitor their activity.

### Grouping payments under guest customers

We use credit card number as the unique identifier to group credit card payments of your guest customers under the same guest identity. See the [guest customer support page](https://support.stripe.com/questions/guest-customer-faq) for additional details on the matching logic. If the same credit card was used by different guest customers (for example, two spouses using the same credit card to checkout at different times), all guest payments for that credit card show up together under one guest customer. Because we group by credit card, we consider it the same guest customer.

### Updating your privacy policy or other privacy notices

You’re in the best position to know whether this feature is consistent with your privacy policy or other privacy notices. It’s a good practice to review your privacy notices and privacy policy when considering any new feature. Guest customers give you a view of your existing guest data, which can help you better detect fraud and help you manage customer service inquiries.

### Exporting guest customer data from the Dashboard

You can export guest customer data from the [Customers](https://dashboard.stripe.com/customers) tab in the Dashboard. Guest customer information isn’t included in exports from the [Payments](https://dashboard.stripe.com/payments) tab.

### Not seeing any guest customers in the Guests tab

If you don’t see any guest customers under the **Guests** tab, this is because your Stripe integration is passing a Customer ID when creating Checkout Sessions. We only create guest customers for payments without a specific Customer object associated with them.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/save-and-reuse

 Set up future payments | Stripe Documentation     

[Skip to content](#main-content)

Set up future payments

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fsave-and-reuse)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fsave-and-reuse)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

Set up future payments

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

India

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

Set up future payments
======================

Learn how to save payment details and charge your customers later.
------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

To collect customer payment details that you can reuse later, use Checkout’s setup mode. Setup mode uses the [Setup Intents API](/api/setup_intents) to create [Payment Methods](/api/payment_methods).

Check out our [full, working sample on GitHub](https://github.com/stripe-samples/checkout-remember-me-with-twilio-verify).

[

Set up Stripe

Server-side




------------------------------





](#set-up-stripe)

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries to access the Stripe API from your application:

Command Line

Select a languageRuby

`# Available as a gem sudo gem install stripe`

Gemfile

Select a languageRuby

`# If you use bundler, you can add this line to your Gemfile gem 'stripe'`

[

Create a Checkout Session

Client-side

Server-side




-------------------------------------------------------





](#create-checkout-session)

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

index.html

`<html>   <head>     <title>Checkout</title>   </head>   <body>     <form action="/create-checkout-session" method="POST">       <button type="submit">Checkout</button>     </form>   </body> </html>`

To create a setup mode Session, use the `mode` parameter with a value of `setup` when creating the Session. You can optionally specify the [customer parameter](/api/checkout/sessions/create#create_checkout_session-customer) to automatically attach the created payment method to an existing customer. Checkout uses [Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods) by default, which requires you to pass the [currency](/api/checkout/sessions/create#create_checkout_session-currency) parameter when using `setup` mode.

Append the `{CHECKOUT_SESSION_ID}` template variable to the `success_url` to get access to the Session ID after your customer successfully completes a Checkout Session. After creating the Checkout Session, redirect your customer to the [URL](/api/checkout/sessions/object#checkout_session_object-url) returned in the response.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_tR3PYbcVNZZ796tH88S4VQ2u  :" \  -d mode=setup \  -d currency=usd \  -d customer=  {{CUSTOMER_ID}}   \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})"`

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn individual payment methods on or off in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). By default, Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe filters them out even when they’re enabled. We filter Google Pay if you [enable automatic tax](/tax/checkout) without collecting a shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

[

Retrieve the Checkout Session

Server-side




----------------------------------------------





](#retrieve-checkout-session)

After a customer successfully completes their Checkout Session, you need to retrieve the Session object. There are two ways to do this:

*   **Asynchronously**: Handle `checkout.session.completed` [webhooks](/webhooks "webhook"), which contain a Session object. Learn more about [setting up webhooks](/webhooks).
*   **Synchronously**: Obtain the Session ID from the `success_url` when a user redirects back to your site. Use the Session ID to [retrieve](/api/checkout/sessions/retrieve) the Session object.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions/cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k \  -u "  sk_test_tR3PYbcVNZZ796tH88S4VQ2u  :"`

The right choice depends on your tolerance for dropoff, as customers may not always reach the `success_url` after a successful payment. It’s possible for them close their browser tab before the redirect occurs. Handling webhooks prevents your integration from being susceptible to this form of dropoff.

After you have retrieved the Session object, get the value of the `setup_intent` key, which is the ID for the SetupIntent created during the Checkout Session. A [SetupIntent](/payments/setup-intents) is an object used to set up the customer’s bank account information for future payments.

Example `checkout.session.completed` payload:

`{   "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",   "object": "event",   "api_version": "2019-03-14",   "created": 1561420781,   "data": {     "object": {       "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",       "object": "checkout.session",       "billing_address_collection": null,       "client_reference_id": null,       "customer": "",       "customer_email": null,       "display_items": [],       "mode": "setup",       "setup_intent": "seti_1EzVO3HssDVaQm2PJjXHmLlM",       "submit_type": null,       "subscription": null,       "success_url": "[https://example.com/success](https://example.com/success)"     }   },   "livemode": false,   "pending_webhooks": 1,   "request": {     "id": null,     "idempotency_key": null   },   "type": "checkout.session.completed" }`

Note the `setup_intent` ID for the next step.

[

Retrieve the SetupIntent

Server-side




-----------------------------------------





](#retrieve-setup-intent)

Using the `setup_intent` ID, [retrieve](/api/setup_intents/retrieve) the SetupIntent object. The returned object contains a `payment_method` ID that you can attach to a customer in the next step.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/setup_intents/seti_1EzVO3HssDVaQm2PJjXHmLlM \  -u "  sk_test_tR3PYbcVNZZ796tH88S4VQ2u  :"`

#### Note

If you’re requesting this information synchronously from the Stripe API (as opposed to handling webhooks), you can combine the previous step with this step by [expanding](/api/expanding_objects) the SetupIntent object in the request to the /v1/checkout/session endpoint. Doing this prevents you from having to make two network requests to access the newly created PaymentMethod ID.

[

Charge the payment method later

Server-side




------------------------------------------------





](#charge-saved-payment-method)

If you didn’t create the Checkout Session with an existing customer, use the ID of the PaymentMethod to [attach](/api/payment_methods/attach) the [PaymentMethod](/api/payment_methods "PaymentMethods") to a [Customer](/api/customers "Customers"). After you attach the PaymentMethod to a customer, you can make an off-session payment using a [PaymentIntent](/api/payment_intents/create#create_payment_intent-payment_method):

*   Set [customer](/api#create_payment_intent-customer) to the ID of the Customer and [payment\_method](/api#create_payment_intent-payment_method) to the ID of the PaymentMethod.
*   Set [off\_session](/api/payment_intents/confirm#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during a payment attempt and can’t fulfill an authentication request made by a partner, such as a card issuer, bank, or other payment institution. If, during your checkout flow, a partner requests authentication, Stripe requests exemptions using customer information from a previous on-session transaction. If the conditions for exemption aren’t met, the PaymentIntent might throw an error.
*   Set the value of the PaymentIntent’s [confirm](/api/payment_intents/create#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when you create the PaymentIntent.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/payment_intents \  -u "  sk_test_tR3PYbcVNZZ796tH88S4VQ2u  :" \  -d amount=1099 \  -d currency=usd \  -d customer=  {{CUSTOMER_ID}}   \  -d payment_method=  {{PAYMENT_METHOD_ID}}   \  -d off_session=true \  -d confirm=true`

When a payment attempt fails, the request also fails with a 402 HTTP status code and the status of the PaymentIntent is [requires\_payment\_method](/upgrades#2019-02-11 "requires_payment_method"). Notify your customer to return to your application (for example, by sending an email or in-app notification) and direct your customer to a new Checkout Session to select another payment method.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_tR3PYbcVNZZ796tH88S4VQ2u  :" \  -d customer=  {{CUSTOMER_ID}}   \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][unit_amount]"=1099 \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})"`

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Set up Stripe](#set-up-stripe "Set up Stripe")

[Create a Checkout Session](#create-checkout-session "Create a Checkout Session")

[Payment methods](#payment-methods "Payment methods")

[Retrieve the Checkout Session](#retrieve-checkout-session "Retrieve the Checkout Session")

[Retrieve the SetupIntent](#retrieve-setup-intent "Retrieve the SetupIntent")

[Charge the payment method later](#charge-saved-payment-method "Charge the payment method later")

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/after-the-payment?oo-step=true&should-crawl=true&record-id=yppw5efx13&wait-before-scraping=2000&save-html=true&save-markdown=true

 After the payment | Stripe Documentation      

[Skip to content](#main-content)

After the payment

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fafter-the-payment)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fafter-the-payment)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

After the payment

[Fulfill orders](/checkout/fulfillment)

[Send receipts and paid invoices](/payments/checkout/receipts)

[Customize redirect behavior](/payments/checkout/custom-success-page)

[Recover abandoned carts](/payments/checkout/abandoned-carts)

[Analyze conversion funnel](/payments/checkout/analyze-conversion-funnel)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

After the payment
=================

Customize the post-payment checkout process.
--------------------------------------------

[

Fulfill orders

Handle post-checkout tasks, such as fulfilling orders and shipping products.

](/checkout/fulfillment "Fulfill orders")

[

Customize redirect behavior

Display a confirmation page with your customer’s order information.

](/payments/checkout/custom-success-page "Customize redirect behavior")

[

Recover abandoned carts

Recover abandoned checkout pages and boost revenue.

](/payments/checkout/abandoned-carts "Recover abandoned carts")

[

Analyze your conversion funnel

Analyze your Stripe Checkout conversion funnel with Google Analytics 4.

](/payments/checkout/analyze-conversion-funnel "Analyze your conversion funnel")

[

Send email receipts and paid invoices

Send payment or refund receipts automatically.

](/payments/checkout/receipts "Send email receipts and paid invoices")

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/custom-fields

 Add custom fields | Stripe Documentation     

[Skip to content](#main-content)

Add custom fields

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-fields)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-fields)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect physical addresses](/payments/collect-addresses "Learn how to collect billing and shipping addresses.")

[Charge for shipping](/payments/during-payment/charge-shipping)

[Collect phone numbers](/payments/checkout/phone-numbers "Collect customer phone numbers with Checkout")

Add custom fields

[Collect consent for promotional emails](/payments/checkout/promotional-emails-consent)

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Netherlands

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Collect additional information](/payments/checkout/collect-additional-info "Collect additional information")

Add custom fields
=================

Add additional fields to a prebuilt payment page with Checkout.
---------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

You can add custom fields on the payment form to collect additional information from your customers. The information is available after the payment is complete and is useful for fulfilling the purchase.

Custom fields have the following limitations:

*   Up to three fields allowed.
*   Not available in `setup` mode.
*   Support for up to 255 characters on text fields.
*   Support for up to 255 digits on numeric fields.
*   Support for up to 200 options on dropdown fields.

#### Caution

Don’t use custom fields to collect personal, protected, or sensitive data, or information restricted by law.

[

Create a Checkout Session


---------------------------





](#create-session)

Create a Checkout Session while specifying an array of [custom fields](/api/checkout/sessions/create#create_checkout_session-custom_fields). Each field must have a unique `key` that your integration uses to reconcile the field. Also provide a label for the field that you display to your customer. Labels for custom fields aren’t translated, but you can use the [locale](/api/checkout/sessions/create#create_checkout_session-locale) parameter to set the language of your Checkout Session to match the same language as your labels.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "custom_fields[0][key]"=engraving \  -d "custom_fields[0][label][type]"=custom \  -d "custom_fields[0][label][custom]"="Personalized engraving" \  -d "custom_fields[0][type]"=text`

![A checkout page with custom fields](https://b.stripecdn.com/docs-statics-srv/assets/required.ba6d59544fa4519cf4eb2a1764e016cf.png)

[

Retrieve custom fields


------------------------





](#retrieve-fields)

When your customer completes the Checkout Session, we send a [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) [webhook](/webhooks "webhook") with the completed fields.

Example `checkout.session.completed` payload:

`{   "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",   "object": "event",   "api_version": "2022-11-15",   "created": 1664928000,   "data": {     "object": {       "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",       "object": "checkout.session",       "custom_fields": [{         "key": "engraving",         "label": {           "type": "custom",           "custom": "Personalized engraving"         },         "optional": false,         "type": "text",         "text": {           "value": "Jane",         }       }],       "mode": "payment",     }   },   "livemode": false,   "pending_webhooks": 1,   "request": {     "id": null,     "idempotency_key": null   },   "type": "checkout.session.completed" }`

[

Use a custom field


--------------------





](#use-custom-field)

### Mark a field as optional

By default, customers must complete all fields before completing payment. To mark a field as optional, pass in `optional=true`.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "custom_fields[0][key]"=engraving \  -d "custom_fields[0][label][type]"=custom \  -d "custom_fields[0][label][custom]"="Personalized engraving" \  -d "custom_fields[0][type]"=text \  -d "custom_fields[0][optional]"=true`

![](https://b.stripecdn.com/docs-statics-srv/assets/optional.bf0c1564296ff02264bd5e8c066a6034.png)

### Add a dropdown field

A dropdown field presents your customers with a list of options to select from. To create a dropdown field, specify `type=dropdown` and a list of options, each with a `label` and a `value`. The `label` displays to the customer while your integration uses the `value` to reconcile which option the customer selected.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "custom_fields[0][key]"=sample \  -d "custom_fields[0][label][type]"=custom \  -d "custom_fields[0][label][custom]"="Free sample" \  -d "custom_fields[0][optional]"=true \  -d "custom_fields[0][type]"=dropdown \  -d "custom_fields[0][dropdown][options][0][label]"="Balm sample" \  -d "custom_fields[0][dropdown][options][0][value]"=balm \  -d "custom_fields[0][dropdown][options][1][label]"="BB cream sample" \  -d "custom_fields[0][dropdown][options][1][value]"=cream`

![A checkout page with a dropdown field](https://b.stripecdn.com/docs-statics-srv/assets/dropdown.4501d199ebe009030c2be6935cfdf2dd.png)

### Add a numbers only field

A numbers-only field provides your customers a text field that only accepts numerical values, up to 255 digits. To create a numbers-only field, specify `type=numeric`.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "custom_fields[0][key]"=invoice \  -d "custom_fields[0][label][type]"=custom \  -d "custom_fields[0][label][custom]"="Invoice number" \  -d "custom_fields[0][type]"=numeric`

### Retrieve custom fields for a subscription

You can retrieve the custom fields associated with a subscription by querying for the Checkout Session that created it using the [subscription](/api/checkout/sessions/list#list_checkout_sessions-subscription) parameter.

Command Line

cURL

`curl -G https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d subscription=  {{SUBSCRIPTION_ID}}    `

### Add character length validations

You can optionally specify a minimum and maximum character length [requirement](/api/checkout/sessions/create#create_checkout_session-custom_fields-numeric-maximum_length) for `text` and `numeric` field types.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "custom_fields[0][key]"=engraving \  -d "custom_fields[0][label][type]"=custom \  -d "custom_fields[0][label][custom]"="Personalized engraving" \  -d "custom_fields[0][type]"=text \  -d "custom_fields[0][text][minimum_length]"=10 \  -d "custom_fields[0][text][maximum_length]"=20 \  -d "custom_fields[0][optional]"=true`

![A field with character limits](https://b.stripecdn.com/docs-statics-srv/assets/between-validation.20431cd8e0c03a028843945d1f1ea314.png)

### Add default values

You can optionally provide a default value for the [text](/api/checkout/sessions/create#create_checkout_session-custom_fields-text-default_value), [numeric](/api/checkout/sessions/create#create_checkout_session-custom_fields-numeric-default_value), and [dropdown](/api/checkout/sessions/create#create_checkout_session-custom_fields-dropdown-default_value) field types. Default values are prefilled on the payment page.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "custom_fields[0][key]"=engraving \  -d "custom_fields[0][label][type]"=custom \  -d "custom_fields[0][label][custom]"="Personalized engraving" \  -d "custom_fields[0][type]"=text \  -d "custom_fields[0][text][default_value]"=Stella \  -d "custom_fields[1][key]"=size \  -d "custom_fields[1][label][type]"=custom \  -d "custom_fields[1][label][custom]"=Size \  -d "custom_fields[1][type]"=dropdown \  -d "custom_fields[1][dropdown][default_value]"=small \  -d "custom_fields[1][dropdown][options][0][value]"=small \  -d "custom_fields[1][dropdown][options][0][label]"=Small \  -d "custom_fields[1][dropdown][options][1][value]"=large \  -d "custom_fields[1][dropdown][options][1][label]"=Large`

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Create a Checkout Session](#create-session "Create a Checkout Session")

[Retrieve custom fields](#retrieve-fields "Retrieve custom fields")

[Use a custom field](#use-custom-field "Use a custom field")

[Mark a field as optional](#optional "Mark a field as optional")

[Add a dropdown field](#dropdown "Add a dropdown field")

[Add a numbers only field](#numeric "Add a numbers only field")

[Retrieve custom fields for a subscription](#subscription "Retrieve custom fields for a subscription")

[Add character length validations](#validation "Add character length validations")

[Add default values](#default-value "Add default values")

Products Used

[

Checkout





](/payments/checkout)

[

Payments





](/payments)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/pricing-table?oo-step=true&should-crawl=true&record-id=7jvgfwdarg&wait-before-scraping=2000&save-html=true&save-markdown=true

 Embeddable pricing table for SaaS businesses | Documentazione Stripe      

[Passa al contenuto](#main-content)

Incorpora una tabella dei prezzi

[

Crea account



](https://dashboard.stripe.com/register/billing)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpricing-table)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register/billing)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpricing-table)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/finance-automation)

Addebito

[Panoramica](/billing)

[Informazioni sulle API di Billing](/billing/billing-apis)

[Abbonamenti](/subscriptions)

[Panoramica](/billing/subscriptions/overview "Informazioni sui cicli di vita degli abbonamenti e delle fatture di Stripe Billing")

[Avvio rapido](/billing/quickstart "Avvio rapido")

[Casi d'uso](/billing/subscriptions/use-cases)

[Creare integrazioni](/billing/subscriptions/integration)

[Funzionalità di abbonamento](/billing/subscriptions/features)

[Fatture degli abbonamenti](/billing/invoices/subscription "Come gestire le fatture degli abbonamenti")

[Pianificazioni degli abbonamenti](/billing/subscriptions/subscription-schedules "Informazioni sui programmi di abbonamento e come utilizzarli")

Tariffe per abbonamenti

[Modelli di prezzo ricorrente](/products-prices/pricing-models "Informazioni sui modelli per i prezzi ricorrenti")

Incorpora una tabella dei prezzi

Avviare abbonamenti

[Impostare quantità](/billing/subscriptions/quantities "Diversificare il costo di un abbonamento iscrivendo un cliente a più quantità di un prodotto")

[Impostazione cicli di addebito](/billing/subscriptions/billing-cycle "Come impostare la data di addebbito per gli abbonamenti")

[Retrodatazione abbonamenti](/billing/subscriptions/backdating "Addebita ai clienti un importo basato sulle scadenze.")

[Abbonarsi a più elementi](/billing/subscriptions/multiple-products "Crea abbonamenti con più prodotti, con fattura unica per tutti i pagamenti.")

[Impostare periodi di prova](/billing/subscriptions/trials "Configura pagamenti ritardati per gli abbonamenti attivi utilizzando periodi di prova.")

[Applicazione di coupon](/billing/subscriptions/coupons "Aggiungere sconti a un abbonamento utilizzando coupon e codici promozionali")

[Eseguire la migrazione degli abbonamenti in Stripe](/billing/subscriptions/migrate-subscriptions "Importare abbonamenti in Stripe da altre fonti")

Pagamenti in abbonamento

[Modalità di pagamento per abbonamenti](/billing/subscriptions/payment-methods-setting "Scopri come specificare le modalità di pagamento consentite per un abbonamento.")

[Eseguire l'integrazione con elaborazione di pagamenti di terze parti](/billing/subscriptions/third-party-payment-processing "Utilizzare abbonamenti e fatture con elaboratori di pagamento terzi")

[Modalità di riscossione](/billing/collection-method "Configurare il metodo preferito per la riscossione di fatture e abbonamenti")

[Condividere un link per aggiornare i dati di pagamento](/billing/subscriptions/update-payment-method "Fornire ai clienti dei link per aggiornare i dati di pagamento per gli abbonamenti")

[Autenticazione forte del cliente (SCA)](/billing/migration/strong-customer-authentication "Aggiornare l'integrazione per supportare i requisiti di autenticazione SCA")

Gestire gli abbonamenti

[Modificare abbonamenti](/billing/subscriptions/change "Scopri come modificare gli abbonamenti esistenti.")

[Gestione aggiornamenti in sospeso](/billing/subscriptions/pending-updates "Come gestire i pagamenti non riusciti durante l'aggiornamento di un abbonamento")

[Analisi](/billing/subscriptions/analytics "Utilizzare la Dashboard per visualizzare le metriche relative agli abbonamenti")

[Invoicing](/invoicing "Creare e gestire fatture per pagamenti una tantum")

[Addebito a consumo](/billing/subscriptions/usage-based)

[Connect e Billing](/billing/multi-entity-business)

[Tax e Billing](/billing/taxes)

[Preventivi](/quotes "Informazioni sui preventivi")

[Recupero dei ricavi](/billing/revenue-recovery "Ulteriori informazioni sulle funzionalità automatizzate di recupero dei ricavi per gli abbonamenti")

[Automazioni](/billing/automations)

[Riconoscimento dei ricavi](/revenue-recognition/methodology/subscriptions-and-invoicing "Uso di Revenue Recognition con gli abbonamenti")

[Gestione clienti](/customer-management "Come attivare la gestione autonoma per i clienti")

[Diritti di accesso](/billing/entitlements "Stabilisci quando concedere e revocare l'accesso dei clienti alle funzionalità del tuo prodotto.")

[Esegui il test della tua integrazione](/billing/testing "Testare l'integrazione di Billing")

Tasse

Reportistica

Dati

Costituzione di start-up

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Automazione finanziaria](/finance-automation "Automazione finanziaria")Billing[Subscriptions](/subscriptions "Subscriptions")[Subscription features](/billing/subscriptions/features "Subscription features")

Embeddable pricing table for SaaS businesses
============================================

Display a pricing table on your website and take customers directly to Stripe Checkout.
---------------------------------------------------------------------------------------

You can use the Stripe Dashboard to create a table that displays different subscription pricing levels to your customers. You don’t need to write any custom code to create or embed a pricing table. This guide describes how to:

*   Use the Stripe Dashboard to configure the UI component
*   Copy the generated code from the Dashboard
*   Embed the code on your website to show your customers pricing information and take them to a checkout page

Overview
--------

![The pricing table is an embedded UI that displays pricing information and takes customers to checkout.](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-embed.b27a06fcd84b57a8866a8b4b62323fdc.png)

Embed a pricing table on your website to display pricing details and convert customers to checkout.

A pricing table is an embeddable UI that:

*   Displays [pricing information](/products-prices/pricing-models "modello tariffario") and takes customers to a prebuilt checkout flow. The checkout flow uses [Stripe Checkout](/payments/checkout) to complete the purchase.
*   Supports common subscription business models like [flat-rate](/products-prices/pricing-models#flat-rate), [per-seat](/products-prices/pricing-models#per-seat), [tiered pricing](/products-prices/pricing-models#tiered-pricing), and free trials.
*   Lets you configure, customize, and update product and pricing information directly in the Dashboard, without needing to write any code.
*   Embeds into your website with a `<script>` tag and web component. Stripe automatically generates the tag. You copy and paste it into your website’s code.

The diagram below summarizes how the customer goes from viewing a pricing table to completing checkout.

Customer

Your application

Stripe Checkout

Views pricing table

Clicks on “subscribe” button

Completes purchase

Returns to your website

checkout.session.completed

Pricing table

[

Create pricing table


----------------------





](#Create)

1.  In the Dashboard, go to **More** > **Product catalog** > [pricing tables](https://dashboard.stripe.com/pricing-tables).
2.  Click **+Create pricing table**.
3.  Add products relevant to your customers (up to four per pricing interval). Optionally, include a free trial.
4.  Adjust the look and feel in **Display settings**. Highlight a specific product and customize the language, colors, font, and button design, then click **Continue**.
5.  Configure **Payment settings** to select the customer information to collect, options to present to the customer, and whether to display a confirmation page or redirect customers back to your site after a successful purchase.
    
    #### Confirm maximum quantity
    
    If you have tiered pricing that supports quantities greater than the default maximum of 99, check the **Let customers adjust quantity** property and increase the **Max** value accordingly. Tiered pricing options for quantities above the maximum don’t appear in the selector.
    
6.  Configure the [customer portal](/no-code/customer-portal) by clicking **Continue**.
7.  Click **Copy code** to copy the generated code and [embed it into your website](/no-code/pricing-table#embed).

![Customizing a pricing table](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-1.45ac9351d8f043a0a63554b89b2cedfc.png)

Customize your pricing table

![Configure payment settings](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-2.07d5287026b797b9aa1905c6ad99958d.png)

Configure payment settings

[

Embed pricing table


---------------------





](#embed)

After creating a pricing table, Stripe automatically returns an embed code composed of a `<script>` tag and a `<stripe-pricing-table>` web component. Click the **Copy code** button to copy the code and paste it into your website.

![Pricing table detail page](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-detail-page.dee9a93d69e802759dabd0e4ce62f1bd.png)

Copy the pricing table’s code and embed it on your website.

If you’re using HTML, paste the embed code into the HTML. If you’re using React, include the `script` tag in your `index.html` page to mount the `<stripe-pricing-table>` component.

#### Attenzione

The pricing table uses your account’s [publishable API key](/keys). If you revoke the API key, you need to update the embed code with your new publishable API key.

pricing-page.html

HTML

`<body>   <h1>We offer plans that help any business!</h1>   <!-- Paste your embed code script here. -->   <script     async     src="[https://js.stripe.com/v3/pricing-table.js](https://js.stripe.com/v3/pricing-table.js)">   </script>   <stripe-pricing-table     pricing-table-id=  '{{PRICING_TABLE_ID}}'      publishable-key=  "pk_test_XUIpXpyaGuuw0Dc9Ng80xFWs"    >   </stripe-pricing-table> </body>`

[

Track subscriptions


---------------------





](#track-subscriptions)

When a customer purchases a subscription, you’ll see it on the [subscriptions page](https://dashboard.stripe.com/subscriptions) in the Dashboard.

### Handle fulfillment with the Stripe API

The pricing table component uses Stripe Checkout to render a prebuilt, hosted payment page. When a payment is completed using Checkout, Stripe sends the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event. Register an [event destination](/event-destinations) to receive the event at your endpoint to process fulfillment and reconciliation. See the [Checkout fulfillment guide](/checkout/fulfillment) for more details.

The `<stripe-pricing-table>` web component supports setting the `client-reference-id` property. When the property is set, the pricing table passes it to the Checkout Session’s [client\_reference\_id](/api/checkout/sessions/object#checkout_session_object-client_reference_id) attribute to help you reconcile the Checkout Session with your internal system. This can be an authenticated user ID or a similar string. `client-reference-id` can be composed of alphanumeric characters, dashes, or underscores, and be any value up to 200 characters. Invalid values are silently dropped and your pricing table will continue to work as expected.

#### Attenzione

Since the pricing table is embedded on your website and is accessible to anyone, check that `client-reference-id` does not include sensitive information or secrets, such as passwords or API keys.

pricing-page.html

HTML

`<body>   <h1>We offer plans that help any business!</h1>   <!-- Paste your embed code script here. -->   <script     async     src="[https://js.stripe.com/v3/pricing-table.js](https://js.stripe.com/v3/pricing-table.js)">   </script>   <stripe-pricing-table     pricing-table-id=  '{{PRICING_TABLE_ID}}'      publishable-key=  "pk_test_XUIpXpyaGuuw0Dc9Ng80xFWs"      client-reference-id="{{CLIENT_REFERENCE_ID}}"   >   </stripe-pricing-table> </body>`

[

FacoltativoAdd product marketing features


-------------------------------------------





](#product-marketing-features)

[

FacoltativoAdd a custom call-to-action


----------------------------------------





](#custom-cta)

[

FacoltativoPass the customer email


------------------------------------





](#customer-email)

[

FacoltativoPass an existing customer


--------------------------------------





](#customer-session)

[

FacoltativoCustomize the post-purchase experience


---------------------------------------------------





](#post-purchase-experience)

[

FacoltativoUpdate pricing table


---------------------------------





](#update)

[

FacoltativoConfigure free trials


----------------------------------





](#free-trials)

[

FacoltativoContent Security Policy


------------------------------------





](#csp)

[

FacoltativoLet customers manage their subscriptions

No code




----------------------------------------------------------------





](#customer-portal)

[

FacoltativoPresent local currencies


-------------------------------------





](#price-localization)

[

FacoltativoAdd custom fields


------------------------------





](#custom-fields)

Limitations
-----------

*   **Business models**—The pricing table supports common subscription business models like flat-rate, per-seat, tiered pricing, and trials. Other [advanced pricing models](/billing/subscriptions/usage-based/pricing-models) aren’t supported.
*   **Product and price limits**—You can configure the pricing table to display a maximum of four products, with up to three prices per product. You can only configure three unique pricing intervals across all products.
*   **Account creation**—The pricing table call-to-action takes customers directly to checkout. It doesn’t currently support adding an intermediate step (for example, asking the customer to create an account on your website before checking out).
*   **Rate limit**—The pricing table has a [rate limit](/rate-limits) of up to 50 read operations per second. If you have multiple pricing tables, the rate limit is shared.
*   **Checkout redirect**—The pricing table can’t redirect customers to checkout if your website provider sandboxes the embed code in an iframe without the `allow-top-navigation` attribute enabled. Contact your website provider to enable this setting.
*   **Testing the pricing table locally**—The pricing table requires a website domain to render. To test the pricing table locally, run a local HTTP server to host your website’s `index.html` file over the `localhost` domain. To run a local HTTP server, use Python’s [SimpleHTTPServer](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server#running_a_simple_local_http_server) or the [http-server](https://www.npmjs.com/package/http-server) npm module.
*   **Connect**—The pricing table isn’t designed to work with [Connect](/connect "Connect") and doesn’t support features like a platform collecting fees.

Limit customers to one subscription
-----------------------------------

You can redirect customers that already have a subscription to the [customer portal](/billing/subscriptions/customer-portal "portale cliente") or your website to manage their subscription. Learn more about [limiting customers to one subscription](/payments/checkout/limit-subscriptions).

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Overview](#overview "Overview")

[Create pricing table](#Create "Create pricing table")

[Embed pricing table](#embed "Embed pricing table")

[Track subscriptions](#track-subscriptions "Track subscriptions")

[Handle fulfillment with the Stripe API](#handle-fulfillment-with-the-stripe-api "Handle fulfillment with the Stripe API")

[Limitations](#limitations "Limitations")

[Limit customers to one subscription](#limit-subscriptions "Limit customers to one subscription")

Prodotti utilizzati

[

Billing





](/billing)

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/custom-shipping-options

 Dynamically customize shipping options | Stripe Documentation     

[Skip to content](#main-content)

Dynamically customize shipping options

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-shipping-options)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-shipping-options)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

Dynamically customize shipping options

[Dynamically update line items](/payments/checkout/dynamically-update-line-items)

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Dynamically update checkout](/payments/checkout/dynamic-updates "Dynamically update checkout")

Dynamically customize shipping optionsPrivate preview
=====================================================

Update shipping options based on a customer's shipping address.
---------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Dynamic updates aren’t available with Stripe-hosted pages.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/migration

 Checkout migration guide | Stripe Documentation     

[Skip to content](#main-content)

Build a checkout page

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigration)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigration)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

Migrate from legacy Checkout

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Switzerland

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

Checkout migration guide
========================

Learn how to migrate to Stripe's latest integrations.
-----------------------------------------------------

![](https://b.stripecdn.com/docs-statics-srv/assets/migration.4db0b4061fb36d6a43762c3f23ef9c00.png)

The legacy version of Checkout presented customers with a modal dialog that collected card information, and returned a token or a source to your website. In contrast, [Payment Links](/payment-links) and the current version of [Checkout](/payments/checkout) are smart payment pages hosted by Stripe that creates payments or [subscriptions](/billing/subscriptions/creating "subscriptions"). Both integrations support Apple Pay, Google Pay, Dynamic [3D Secure](/payments/3d-secure "3D Secure (3DS)"), [Connect](/connect "Connect"), re-using existing [Customers](/api/customers "Customers"), and many other features. You can also [compare other payment integrations](/payments/online-payments#compare-features-and-availability) if Payment Links or Checkout doesn’t fit your use case.

Before you begin
----------------

If you use Stripe’s [SDKs](/sdks), upgrade to the latest version.

Choose your business model
--------------------------

To migrate from the legacy version of Checkout, follow the guide that most closely represents your business model. Each guide recommends an integration path along with example code.

*   [Dynamic product catalog and pricing](#api-products)
    
    If you have a large product catalog or require support for dynamically generated line items (such as donations or taxes).
    
*   [Dynamic subscriptions](#api-subscriptions)
    
    If you’re a SaaS provider billing users and need support for advanced features.
    
*   [Connect platforms and marketplaces](#connect)
    
    If you’re operating a marketplace connecting service providers with customers.
    
*   [Saving payment methods for future use](#setup-mode)
    
    If you’re operating a business which doesn’t charge the customer until after services rendered.
    
*   [Simple product catalog with fixed pricing](#simple-products)
    
    If you’re selling a few products with pre-determined prices.
    
*   [Simple subscriptions](#simple-subscriptions)
    
    If you’re a SaaS provider with a monthly subscription plan.
    

As you follow the relevant migration guide, you can also reference the [conversion table](#parameter-conversion) for a mapping of specific parameters and configuration options.

Dynamic product catalog and pricing
-----------------------------------

If you’re selling products where the amount or line items are determined dynamically (for example, a large product catalog or donations), see [accepting one-time payments](/payments/accept-a-payment?integration=checkout).

You might have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a charge. The current version of Checkout reverses this flow—you create a Session on your server, redirect your customer to Checkout, who is then redirected back to your application after the payment.

### Before

With the legacy version of Checkout, you’d display the dynamic amount and description and collect card information from your customer.

client.html

`<form action="/purchase" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_LMUiQyn0mBZPsUIhVrVMblov"      data-name="Custom t-shirt"     data-description="Your custom designed t-shirt"     data-amount="{{ORDER_AMOUNT}}"     data-currency="usd">   </script> </form>`

Next, you’d send the resulting token or source to your server and charge it.

Command Line

curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "email"="customer@example.com" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/charges \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "description"="Custom t-shirt" \   -d "amount"="{{ORDER_AMOUNT}}" \   -d "currency"="usd"`

### After

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](/api/checkout/sessions/create).

checkout.html

`<html>   <head>     <title>Buy cool new product</title>   </head>   <body>     <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->     <form action="/create-checkout-session" method="POST">       <button type="submit">Checkout</button>     </form>   </body> </html>`

A Checkout Session is the programmatic representation of what your customer sees when they’re redirected to the payment form. You can configure it with options such as:

*   [Line items](/api/checkout/sessions/create#create_checkout_session-line_items) to charge
*   Currencies to use

Include a `success_url` with the URL of a page on your website that your customer is redirected to after they complete the payment.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  :" \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][price_data][product_data][name]"="Custom t-shirt" \  -d "line_items[0][price_data][unit_amount]"=2000 \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

After creating a Checkout Session, redirect your customer to the [URL](/api/checkout/sessions/object#checkout_session_object-url) returned in the response. If you need to fulfill purchased goods after the payment, see [Fulfill Checkout and Payment Link payments](/checkout/fulfillment).

Dynamic subscriptions
---------------------

If you’re providing subscription services that are dynamically determined or require support for other advanced features, see [setting up a subscription](/billing/subscriptions/build-subscriptions).

You might have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a customer and subscription. The current version of Checkout reverses this flow—you first create a Session on your server, redirect your customer to Checkout, who then gets redirected back to your application upon success.

### Before

With the legacy version of Checkout, you’d display the subscription information and collect card information from your customer.

client.html

`<form action="/subscribe" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_LMUiQyn0mBZPsUIhVrVMblov"      data-name="Gold Tier"     data-description="Monthly subscription with 30 days trial"     data-amount="2000"     data-label="Subscribe">   </script> </form>`

Next, you’d send the resulting token or source to your server to create a customer and a subscription.

Command Line

curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "email"="customer@example.com" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/subscriptions \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "items[0][price]"="{PRICE_ID}" \   -d "trial_period_days"=30`

### After

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](/api/checkout/sessions/create).

checkout.html

`<html>   <head>     <title>Subscribe to cool new service</title>   </head>   <body>     <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->     <form action="/create-checkout-session" method="POST">       <button type="submit">Subscribe</button>     </form>   </body> </html>`

A Checkout Session is the programmatic representation of what your customer sees when they’re redirected to the payment form. You can configure it with options such as:

*   [Line items](/api/checkout/sessions/create#create_checkout_session-line_items) to charge
*   Currencies to use

Include a `success_url` with the URL of a page on your website that your customer is redirected to after they complete the payment.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "subscription_data[trial_period_days]"=30 \  -d mode=subscription \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

After creating a Checkout Session, redirect your customer to the [URL](/api/checkout/sessions/object#checkout_session_object-url) returned in the response. The customer is redirected to the `success_url` after the customer and subscription are created. If you need to fulfill purchased services after the payment, see [Fulfill Checkout and Payment Link payments](/checkout/fulfillment).

Connect platforms and marketplaces
----------------------------------

If you’re operating a Connect platform or marketplace and create payments involving connected accounts, consider using the current version Checkout.

The following example demonstrates using the Checkout Sessions API to process a direct charge. You can also use Checkout and Connect with [destination charges](/connect/destination-charges?platform=web&ui=stripe-hosted) and [separate charges and transfers](/connect/separate-charges-and-transfers?platform=web&ui=stripe-hosted).

### Before

With the legacy version of Checkout, you’d collect card information from your customer on the client.

client.html

`<form action="/purchase" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_LMUiQyn0mBZPsUIhVrVMblov"      data-name="Food Marketplace"     data-description="10 cucumbers from Roger's Farm"     data-amount="2000">   </script> </form>`

Next, you’d send the resulting token or source to your server and charge it on behalf of the connected account.

Command Line

curl

`curl https://api.stripe.com/v1/charges \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "source"="{{TOKEN_ID}}" \   -d "description"="10 cucumbers from Roger\"s Farm" \   -d "amount"=2000 \   -d "currency"="usd" \   -d "application_fee_amount"=200 \   -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}"`

### After

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](/api/checkout/sessions/create).

checkout.html

`<html>   <head>     <title>Roger's Farm</title>   </head>   <body>     <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->     <form action="/create-checkout-session" method="POST">       <button type="submit">Checkout</button>     </form>   </body> </html>`

A Checkout Session is the programmatic representation of what your customer sees when they’re redirected to the payment form. You can configure it with options such as:

*   [Line items](/api/checkout/sessions/create#create_checkout_session-line_items) to charge
*   Currencies to use

Include a `success_url` with the URL of a page on your website that your customer is redirected to after they complete the payment.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  :" \  -H "Stripe-Account:   {{CONNECTED_ACCOUNT_ID}}  " \  -d "line_items[0][price_data][currency]"=usd \   --data-urlencode "line_items[0][price_data][product_data][name]"="Cucumbers from Roger's Farm" \  -d "line_items[0][price_data][unit_amount]"=200 \  -d "line_items[0][quantity]"=10 \  -d "payment_intent_data[application_fee_amount]"=200 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

After creating a Checkout Session, redirect your customer to the [URL](/api/checkout/sessions/object#checkout_session_object-url) returned in the response. If you need to fulfill purchased goods or services after the payment, see [Fulfill Checkout and Payment Link payments](/checkout/fulfillment).

Saving payment methods for future use
-------------------------------------

If you’re providing services that don’t charge your customers immediately, see [setting up future payments](/payments/save-and-reuse?platform=checkout).

You might have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to save for later use. The current version of Checkout reverses this flow—you first create a Session on your server, redirect your customer to Checkout, who then gets redirected back to your application upon success.

### Before

With the legacy version of Checkout, you’d display the charge information and collect card information from your customer.

client.html

`<form action="/subscribe" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_LMUiQyn0mBZPsUIhVrVMblov"      data-name="Cleaning Service"     data-description="Charged after your home is spotless"     data-amount="2000">   </script> </form>`

Next, you’d send the resulting token or source to your server to eventually create a charge.

Command Line

curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "email"="customer@example.com" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/charges \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "description"="Cleaning service" \   -d "amount"="{{ORDER_AMOUNT}}" \   -d "currency"="usd"`

### After

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](/api/checkout/sessions/create).

checkout.html

`<html>   <head>     <title>Cleaning service</title>   </head>   <body>     <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->     <form action="/create-checkout-session" method="POST">       <button type="submit">Subscribe</button>     </form>   </body> </html>`

A Checkout Session is the programmatic representation of what your customer sees when they’re redirected to the payment form. You can configure it with options such as:

*   [Line items](/api/checkout/sessions/create#create_checkout_session-line_items) to charge
*   Currencies to use

Include a `success_url` with the URL of a page on your website that your customer is redirected to after they complete the payment setup.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  :" \  -d mode=setup \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})"`

After creating a Checkout Session, redirect your customer to the [URL](/api/checkout/sessions/object#checkout_session_object-url) returned in the response to gather payment method details. The customer is redirected to the `success_url` after they complete the flow. When you’re ready to collect a payment, [retrieve the SetupIntent](/payments/checkout/save-and-reuse?payment-ui=stripe-hosted#retrieve-checkout-session) from the Checkout Session and use it to prepare the transaction.

Simple product catalog with fixed pricing
-----------------------------------------

If you’re selling products with fixed pricing (such as t-shirts or e-books), see the guide on [payment links](/payment-links/create). You might have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a charge.

### Before

With the legacy version of Checkout, you’d display the amount and description and collect card information from your customer.

client.html

`<form action="/pay" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_LMUiQyn0mBZPsUIhVrVMblov"      data-name="T-shirt"     data-description="Comfortable cotton t-shirt"     data-amount="500"     data-currency="usd">   </script> </form>`

Next, you’d send the resulting token or source to your server to create a customer and a charge.

Command Line

Curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "email"="{{STRIPE_EMAIL}}" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/charges \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "description"="T-shirt" \   -d "amount"=500 \   -d "currency"="usd"`

### After

Create a [Product](/api/products) and a [Price](/api/prices) representing the item. The following example creates the Product inline. You can also create these objects in the [Dashboard](https://dashboard.stripe.com/test/products).

Command Line

cURL

`curl https://api.stripe.com/v1/prices \  -u "  sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  :" \  -d currency=usd \  -d unit_amount=500 \  -d "product_data[name]"=T-shirt`

Create a [Payment Link](https://dashboard.stripe.com/payment-links/create) in the Dashboard using the Product and Price. After you create the link, click **Buy button** to configure the design and generate the code that you can copy and paste into your website.

index.html

HTML

`<body>   <h1>Purchase your new kit</h1>   <!-- Paste your embed code script here. -->   <script     async     src="[https://js.stripe.com/v3/buy-button.js](https://js.stripe.com/v3/buy-button.js)">   </script>   <stripe-buy-button     buy-button-id=  '{{BUY_BUTTON_ID}}'      publishable-key=  "pk_test_LMUiQyn0mBZPsUIhVrVMblov"    >   </stripe-buy-button> </body>`

Simple subscriptions
--------------------

If you’re providing a simple subscription service (such as monthly access to software), see the guide on [payment links](/payment-links/create). You might have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a customer and a subscription.

### Before

With the legacy version of Checkout, you’d display the subscription information and collect card information from your customer.

client.html

`<form action="/subscribe" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_LMUiQyn0mBZPsUIhVrVMblov"      data-name="Gold Tier"     data-description="Monthly subscription"     data-amount="2000"     data-currency="usd"     data-label="Subscribe">   </script> </form>`

Next, you’d send the resulting token or source to your server to create a customer and a subscription.

Command Line

Curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "email"="{{STRIPE_EMAIL}}" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/subscriptions \   -u sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "items[][price]"="{PRICE_ID}" \   -d "items[][quantity]"=1`

### After

Create a [Product](/api/products) and a [Price](/api/prices) representing the subscription. The following example creates the Product inline. You can also create these objects in the [Dashboard](https://dashboard.stripe.com/test/products).

Command Line

cURL

`curl https://api.stripe.com/v1/prices \  -u "  sk_test_ESDdbUTrLo4e9SC7uoQqlhd2  :" \  -d currency=usd \  -d unit_amount=2000 \  -d "recurring[interval]"=month \  -d "product_data[name]"="Gold Tier"`

Create a [Payment Link](https://dashboard.stripe.com/payment-links/create) in the Dashboard using the Product and Price. After you create the link, click **Buy button** to configure the design and generate the code that you can copy and paste into your website.

index.html

HTML

`<body>   <h1>Purchase your new kit</h1>   <!-- Paste your embed code script here. -->   <script     async     src="[https://js.stripe.com/v3/buy-button.js](https://js.stripe.com/v3/buy-button.js)">   </script>   <stripe-buy-button     buy-button-id=  '{{BUY_BUTTON_ID}}'      publishable-key=  "pk_test_LMUiQyn0mBZPsUIhVrVMblov"    >   </stripe-buy-button> </body>`

Parameter conversion
--------------------

The current version of Checkout supports most of the functionality of the legacy version of Checkout. However, they don’t share the same API. The following table maps the parameters and configuration options between the legacy version and the current version. For a full list of configuration options, see [Checkout Sessions](/api/checkout/sessions).

Legacy version

Current version

Integration tips

`allowRememberMe`

Not supported

Reuse existing customers by specifying the `customer` parameter when creating a [Checkout Session](/api/checkout/sessions/create). You can also enable [Link](/payments/link/checkout-link) to allow your customers to securely save and reuse their payment information.

`amount`

Automatically calculated as the sum of amounts over all `line_items`

The total amount is the sum of the line items you pass to Checkout.

`billingAddress`

`Session.billing_address_collection`

Checkout automatically collects the billing address when required for fraud-prevention or regulatory purposes. Set this parameter to `required` to always collect the billing address.

`closed`

`cancel_url`

When a customer wants to close Checkout, they either close the browser tab or navigate to the `cancel_url`.

`currency`

`Session.currency`

`description`

`Session.line_items.description` or `product.description`

If you specify a price, Checkout displays an automatically computed description of how often payments occur. If you specify `Session.line_items`, Checkout displays the `name` for each line item.

`email`

`Session.customer_email`

If you already know your customer’s email, you can prefill it with [customer\_email](/api/checkout/sessions/create#create_checkout_session-customer_email) when you create the Checkout Session.

`image`

**Business branding**: Upload your business logo or icon in the Dashboard.

**Product images**: Specify images for each line item with `product.images`.

Checkout uses specific images for your business’s [branding](/payments/checkout/customization/appearance#branding) and for the products you’re selling. Checkout displays your business logo by default and falls back to your business icon alongside your business name.

`key`

No longer a parameter passed to Checkout

`locale`

`Session.locale`

You can specify a supported [locale](/payments/checkout/customization/behavior#localization) when creating a Checkout Session.

`name`

`product.name` for prices specified in `Session.line_items`

If you specify a price, Checkout displays the name of the product that belongs to the price. If you specify `Session.line_items`, Checkout displays the `name` for each line item.

`panelLabel`

`submit_type`

Checkout automatically customizes the button text depending on the items you’re selling. For one-time payments, use [submit\_type](/payments/checkout/customization/behavior#submit-button) to customize the button text.

`shippingAddress`

`session.shipping_address_collection`

[Collect shipping address information](/payments/collect-addresses?payment-ui=checkout) by passing an array of `allowed_countries` that you want to ship to.

`token` or `source`

`success_url`

There’s no longer a callback in JavaScript when the payment completes. As your customer is paying on a different page, set the `success_url` to redirect your customer after they’ve completed payment.

`zipCode`

Automatically collected by Checkout

Checkout automatically collects the postal code when required for fraud-prevention or regulatory purposes.

See also
--------

*   [Add more payment methods](/payments/payment-methods/overview)
*   [Collect addresses and phone numbers](/payments/collect-addresses)

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Before you begin](#before-you-begin "Before you begin")

[Choose your business model](#choose-your-business-model "Choose your business model")

[Dynamic product catalog and pricing](#api-products "Dynamic product catalog and pricing")

[Before](#api-products-before "Before")

[After](#api-products-after "After")

[Dynamic subscriptions](#api-subscriptions "Dynamic subscriptions")

[Before](#api-subscriptions-before "Before")

[After](#api-subscriptions-after "After")

[Connect platforms and marketplaces](#connect "Connect platforms and marketplaces")

[Before](#connect-before "Before")

[After](#connect-after "After")

[Saving payment methods for future use](#setup-mode "Saving payment methods for future use")

[Before](#setup-mode--before "Before")

[After](#setup-mode--after "After")

[Simple product catalog with fixed pricing](#simple-products "Simple product catalog with fixed pricing")

[Before](#simple-products-before "Before")

[After](#simple-products-after "After")

[Simple subscriptions](#simple-subscriptions "Simple subscriptions")

[Before](#simple-subscriptions-before "Before")

[After](#simple-subscriptions-after "After")

[Parameter conversion](#parameter-conversion "Parameter conversion")

[See also](#see-also "See also")

Products Used

[

Checkout





](/payments/checkout)

[

Payment Links





](/payments/payment-links)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=stripe-hosted

 How Checkout works | Documentazione Stripe     

[Passa al contenuto](#main-content)

Come funziona Checkout

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

[Panoramica](/payments/checkout)

Come funziona Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Checkout

How Checkout works
==================

Learn how to use Checkout to collect payments on your website.
--------------------------------------------------------------

Checkout is a low-code payment integration that creates a customizable form for collecting payments.

Checkout’s built-in features allow you to reduce your development time. It supports 40+ payment methods, including [Link](/payments/link), which lets your customers save their payment method for faster checkout. You can accept payments by embedding Checkout directly into your website, redirecting customers to a Stripe-hosted payment page, or creating a customized checkout page with [Stripe Elements](/payments/elements). Checkout supports payments for both [one-time purchases](/payments/online-payments) and [subscriptions](/subscriptions).

You can also customize Checkout and access additional functionality with the [Checkout Sessions API](/api/checkout/sessions) and the Stripe Dashboard. For a complete list of features, see its [built-in and customizable features](/payments/checkout/how-checkout-works#features).

Stripe-hosted page

Embedded form

Embedded components

Public preview

Checkout lifecycle
------------------

1.  When customers are ready to complete their purchase, your application creates a new Checkout Session.
2.  The Checkout Session provides a URL that redirects customers to a Stripe-hosted payment page.
3.  Customers enter their payment details on the payment page and complete the transaction.
4.  After the transaction, a [webhook](/webhooks "webhook") [fulfills the order](/checkout/fulfillment) using the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event.

Client

Server

Stripe API

Stripe Checkout

Send order information

Create Checkout Session

Return Checkout Session

checkout.session.created

Redirect customer to `url` from Checkout Session

Customer completes payment

Customer returns to your application

Handle fulfillment

checkout.session.completed

A diagram of a Stripe-hosted page integration's lifecycle

Low-code integration
--------------------

Checkout requires minimal coding and is the best choice for most integrations because of its prebuilt functionalities and customization options. You can integrate Checkout by creating a Checkout Session and collecting customer payment details. Collect payments by redirecting customers to a [Stripe-hosted payment page](/payments/accept-a-payment?platform=web&ui=stripe-hosted).

[Compare Checkout](/payments/online-payments#compare-features-and-availability) to other Stripe payment options to determine the best one for you. Checkout displays a payment form to collect customer payment information, validates cards, handles errors, and so on.

Built-in and customizable features
----------------------------------

Stripe Checkout has the following built-in and customizable features:

### Built-in features

*   Support for digital wallets and Link
*   Responsive mobile design
*   SCA-ready
*   CAPTCHAs
*   PCI compliance
*   Card validation
*   Error messaging
*   [Adjustable quantities](/payments/checkout/adjustable-quantity)
*   [Automatic tax collection](/tax/checkout)
*   International language support
*   [Adaptive Pricing](/payments/checkout/adaptive-pricing)

### Customizable features

*   [Collect taxes](/payments/checkout/taxes)
*   [Custom branding with colors, buttons, and font](/payments/checkout/customization)
*   [Cross-sells](/payments/checkout/cross-sells)
*   [Global payment methods](/payments/dashboard-payment-methods)
*   [Subscription upsells](/payments/checkout/upsells)
*   [Custom domains](/payments/checkout/custom-domains) (Stripe-hosted page only)
*   [Email receipts](/receipts)
*   [Apply discounts](/payments/checkout/discounts)
*   [Custom success page](/payments/checkout/custom-success-page)
*   [Recover abandoned carts](/payments/checkout/abandoned-carts)
*   [Autofill payment details with Link](/payments/checkout/customization/behavior#link)
*   [Collect Tax IDs](/tax/checkout/tax-ids)
*   [Collect shipping information](/payments/collect-addresses?payment-ui=checkout)
*   [Collect phone numbers](/payments/checkout/phone-numbers)
*   [Set the subscription billing cycle date](/payments/checkout/billing-cycle)

### Custom branding

You can set fonts, colors, icons, and field styles for your Stripe-hosted Checkout page using the [Branding settings](https://dashboard.stripe.com/settings/branding/checkout) in the Dashboard. For more information, see [Customize your integration](/payments/checkout/customization).

### Custom domains

If you use Stripe’s [custom domain feature](/payments/checkout/custom-domains), you can serve Stripe-hosted Checkout pages on a subdomain of your custom domain. Custom domains are a paid feature. For information, see [Pricing and fees](https://stripe.com/pricing).

Checkout Session
----------------

The Checkout Session is a programmatic representation of what your customers see on the checkout page. After creating a Checkout Session, redirect your customers to the Session’s URL to complete the purchase. When customers complete their purchase, you can [fulfill their orders](/checkout/fulfillment) by configuring an [event destination](/event-destinations) to process Checkout Session events. This code snippet from the [quickstart guide](/checkout/quickstart) is an example of how to create a Checkout Session in your application.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

### One-time and recurring payments

Allow customers to make one-time payments or subscribe to a product or service by setting the [mode](/api/checkout/sessions/create#create_checkout_session-mode) parameter in a Checkout Session.

Mode

Purchase type

Payment

One-time purchases

[Subscription](/billing/subscriptions/overview)

*   Recurring purchases
*   Mixed cart: Recurring purchases with one-time purchases

### Mixed cart

Create a mixed cart in Checkout that lets your customers purchase Subscription items and one-time purchase items at the same time. To create a mixed cart, set the `mode` parameter to `subscription` and include the Price IDs, or `price_data`, for each line\_item in the [line\_items](/api/checkout/sessions/create#create_checkout_session-line_items) array. Price IDs come from Price objects created using the Stripe Dashboard or API and allow you to store information about your product catalog in Stripe.

You can also use [price\_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data) to reference information from an external database where you’re hosting price and product details without storing product catalog information on Stripe. For more information, see [Build a subscriptions integration](/billing/subscriptions/build-subscriptions).

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d "line_items[0][price]"={{RECURRING_PRICE_ID}} \   -d "line_items[0][quantity]"=1 \  -d "line_items[1][price]"={{ONE_TIME_PRICE_ID}} \   -d "line_items[1][quantity]"=1 \  -d mode=subscription \   --data-urlencode success_url="https://example.com/success" \   --data-urlencode cancel_url="https://example.com/cancel"`

### Payment methods

You can view, enable, and disable different payment methods in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) at any time. Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. View our [complete list of payment methods](/payments/payment-methods/overview).

### Save payment details and default payment methods

You can [save payment details for future use](/payments/save-and-reuse) by sending an API parameter when you create a Session. Options to save payment details include:

*   **Single payment**: If your Checkout Session uses `payment` mode, set the [payment\_intent\_data.setup\_future\_usage](/payments/payment-intents#future-usage) parameter.
*   **Subscription payment**: If your Checkout Session uses `subscription` mode, Stripe saves the payment method by default.
*   [Multiple saved payment methods](/payments/accept-a-payment?platform=web&ui=checkout#save-payment-method-details): If a customer has multiple payment methods saved, you can store a default payment method to the Customer object’s [default\_payment\_method](/api/customers/object#customer_object-invoice_settings-default_payment_method) field. However, these payment methods don’t appear for return purchases in Checkout.

### Guest customers

The `Customer` object represents a customer of your business, and it helps tracking subscriptions and payments that belong to the same customer. Checkout Sessions that don’t create Customers are associated with [guest customers](/payments/checkout/guest-customers) instead.

Complete a transaction
----------------------

To automate business flows after a transaction has occurred, register an [event destination](/event-destinations) and build a [webhook endpoint handler](/webhooks/quickstart). Consider the following events and automations to enable:

*   Process the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event to fullfill orders when a customer completes their purchase.
*   Process the [checkout.session.expired](/api/events/types#event_types-checkout.session.expired) event to return items to your inventory or send users a cart [abandonment](/payments/checkout/abandoned-carts) email when they don’t make a purchase and their cart expires.

Vedi anche
----------

*   [Checkout quickstart](/checkout/quickstart)
*   [Fulfill your orders](/checkout/fulfillment)
*   [Collect taxes in Checkout](/payments/checkout/taxes)
*   [Manage limited inventory with Checkout](/payments/checkout/managing-limited-inventory)
*   [Automatically convert to local currencies with Adaptive Pricing](/payments/checkout/adaptive-pricing)

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Checkout lifecycle](#lifecycle "Checkout lifecycle")

[Low-code integration](#low-code "Low-code integration")

[Built-in and customizable features](#features "Built-in and customizable features")

[Built-in features](#built-in "Built-in features")

[Customizable features](#customizable "Customizable features")

[Custom branding](#branding "Custom branding")

[Custom domains](#custom-domains "Custom domains")

[Checkout Session](#session "Checkout Session")

[One-time and recurring payments](#checkout-mode "One-time and recurring payments")

[Mixed cart](#mixed-cart "Mixed cart")

[Payment methods](#payment-methods "Payment methods")

[Save payment details and default payment methods](#save-payment-methods "Save payment details and default payment methods")

[Guest customers](#guest-customers "Guest customers")

[Complete a transaction](#complete-transaction "Complete a transaction")

[Vedi anche](#see-also "Vedi anche")

Guide correlate

[

No-code options to accept payments on Stripe



](/no-code)

[

Prebuilt checkout page



](/checkout/quickstart)

[

Learn about payment methods



](/payments/payment-methods/overview)

Prodotti utilizzati

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/dynamically-update-line-items

 Dynamically update line items | Stripe Documentation     

[Skip to content](#main-content)

Dynamically update line items

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fdynamically-update-line-items)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fdynamically-update-line-items)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Dynamically customize shipping options](/payments/checkout/custom-shipping-options)

Dynamically update line items

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Dynamically update checkout](/payments/checkout/dynamic-updates "Dynamically update checkout")

Dynamically update line itemsPrivate preview
============================================

Update line items in response to changes made during checkout.
--------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Dynamic updates aren’t available with Stripe-hosted pages.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/promotional-emails-consent?oo-step=true&should-crawl=true&record-id=xs2x16io6y&wait-before-scraping=2000&save-html=true&save-markdown=true

 Collect consent for promotional emails | Stripe Documentation     

[Skip to content](#main-content)

Collect consent for promotional emails

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpromotional-emails-consent)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpromotional-emails-consent)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect physical addresses](/payments/collect-addresses "Learn how to collect billing and shipping addresses.")

[Charge for shipping](/payments/during-payment/charge-shipping)

[Collect phone numbers](/payments/checkout/phone-numbers "Collect customer phone numbers with Checkout")

[Add custom fields](/payments/checkout/custom-fields)

Collect consent for promotional emails

[Compliant promotional emails](/payments/checkout/compliant-promotional-emails)

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Collect additional information](/payments/checkout/collect-additional-info "Collect additional information")

Collect consent for promotional emailsUS only
=============================================

Learn how to collect permission from customers so that you can send them promotional emails.
--------------------------------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Promotional emails are often sent to inform customers of new products and to share coupons and discounts. For example, you can use them to subscribe customers to company newsletters or [send cart abandonment emails](/payments/checkout/abandoned-carts).

![Collect consent for promotional emails](https://b.stripecdn.com/docs-statics-srv/assets/promotional-consent-collection.444ead1668bd41537b9a07b2dbdc219a.png)

Collect consent from customers to send them promotional emails

To protect consumers from unwanted spam, customers must agree to receiving promotional emails before you can contact them. Checkout helps you collect the necessary consent, where applicable, to send promotional emails. Learn more about [promotional email requirements](/payments/checkout/compliant-promotional-emails).

[

Collect consent


-----------------





](#collect-consent)

You can collect promotional email consent with Stripe Checkout when you create the session:

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_4eC39HqLyjWDarjtT1zdp7dc  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=2 \  -d customer=  {{CUSTOMER_ID}}   \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)" \   --data-urlencode cancel_url="[https://example.com/cancel](https://example.com/cancel)" \  -d "consent_collection[promotions]"=auto`

When `consent_collection.promotions='auto'`, Checkout dynamically displays a checkbox for collecting the customer’s consent to promotional content.

#### Note

When the checkbox is shown, the default state depends on the customer’s country and the country your business is based in. Data privacy laws vary by jurisdiction, so Checkout disables or limits this feature when local regulations prohibit it.

[

Store consent and email address


---------------------------------





](#store-consent)

The Checkout Session’s [consent](/api/checkout/sessions/object#checkout_session_object-consent) attribute records whether or not the session collected promotional consent from the customer.

As customers complete purchases, keep track of which customers consent to promotional content. You can create or update an existing [webhook](/webhooks "webhook") handler to do this. Listen to the `checkout.session.completed` event, check for the `consent.promotions` status, and then store email addresses for customers who give consent.

Node

``// Find your endpoint's secret in your Dashboard's webhook settings const endpointSecret = 'whsec_...';  // Using Express const app = require('express')();  // Use body-parser to retrieve the raw body as a buffer const bodyParser = require('body-parser');  const recordPromotionalEmailConsent = (email, promoConsent) => {   // TODO: fill me in   console.log("Recording promotional email consent", email, promoConsent); }  app.post('/webhook', bodyParser.raw({type: 'application/json'}), (request, response) => {   const payload = request.body;   const sig = request.headers['stripe-signature'];    let event;    try {     event = stripe.webhooks.constructEvent(payload, sig, endpointSecret);   } catch (err) {     return response.status(400).send(`Webhook Error: ${err.message}`);   }    // Handle the checkout.session.completed event   if (event.type === 'checkout.session.completed') {     const session = event.data.object;     const promoConsent = session.consent?.promotions;     const email = session.customer_details.email;      // Record whether or not the customer has agreed to receive promotional emails     recordPromotionalEmailConsent(email, promoConsent)      // Handle order fulfillment   }   response.status(200).end(); });``

After you’ve configured Checkout to collect consent for sending customers promotional content, you can [recover abandoned carts](/payments/checkout/abandoned-carts) by following up with leads for customers that left the checkout flow before completing payment.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Collect consent](#collect-consent "Collect consent")

[Store consent and email address](#store-consent "Store consent and email address")

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/customization/appearance?oo-step=true&should-crawl=true&record-id=jyqmjrnv4w&wait-before-scraping=2000&save-html=true&save-markdown=true

 Customize appearance | Documentazione Stripe     

[Passa al contenuto](#main-content)

Personalizza l'aspetto

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fappearance)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fappearance)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

Personalizza l'aspetto

[Personalizza il testo e le politiche](/payments/checkout/customization/policies)

[Personalizzare la procedura](/payments/checkout/customization/behavior)

[Utilizzare il dominio personalizzato](/payments/checkout/custom-domains)

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page[Customize look and feel](/payments/checkout/customization "Customize look and feel")

Customize appearance
====================

Customize your checkout page's colors, fonts, shapes, and more.
---------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Apply branding
--------------

You can apply custom branding to Checkout. Go to [Branding Settings](https://dashboard.stripe.com/settings/branding/checkout) to:

*   Upload a logo or icon
*   Customize the Checkout page’s background color, button color, font, and shapes

### Branding with Connect

For platforms performing direct charges, and destination charges with `on_behalf_of`, Checkout uses the brand settings of the connected account. For connected accounts without access to the full Stripe Dashboard (includes Express and Custom accounts), platforms can configure the brand settings with the [Accounts](/api/accounts/object#account_object-settings-branding) API.

Change your brand name
----------------------

You can change a Checkout page’s name by modifying the **Business name** field in [Business details settings](https://dashboard.stripe.com/settings/business-details).

You can also [customize the domain name](/payments/checkout/custom-domains) of a Stripe-hosted Checkout page.

Font compatibility
------------------

Each custom font is compatible with a [subset of locales](/js/appendix/supported_locales). You can either explicitly set the locale of a Checkout Session by passing the locale field when creating the Session, or use the default `auto` setting where Checkout chooses a locale based on the customer’s browser settings.

The following table lists unsupported locales for each font. Languages in these locales might fall outside of the supported character range for a given font. In those cases, Stripe renders the Checkout page with an appropriate system fallback font. If you choose a Serif font but it’s unsupported in a locale, Stripe falls back to a Serif-based font.

Font family

Unsupported locales

Be Vietnam Pro

`bg`, `el`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Bitter

`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Chakra Petch

`bg`, `el`, `ja`, `ko`, `ru`, `zh`, `zh-HK`, `zh-TW`

Hahmlet

`bg`, `el`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Inconsolata

`bg`, `el`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Inter

`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Lato

`bg`, `cs`, `el`, `hr`, `ja`, `ko`, `lt`, `lv`, `mt`, `ro`, `ru`, `sl`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`

Lora

`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

M PLUS 1 Code

`bg`, `el`, `ko`, `lt`, `lv`, `ru`, `sk`, `sl`, `th`, `tr`

Montserrat

`el`, `hr`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Nunito

`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Noto Sans

`ja`, `ko`, `th`

Noto Serif

`th`

Open Sans

`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

PT Sans

`el`, `ja`, `ko`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`

PT Serif

`el`, `ja`, `ko`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`

Pridi

`bg`, `el`, `ja`, `ko`, `ru`, `zh`, `zh-HK`, `zh-TW`

Raleway

`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Roboto

`ja`, `ko`, `zh`, `zh-HK`, `zh-TW`

Roboto Slab

`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Source Sans Pro

`bg`, `el`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`

Titillium Web

`bg`, `el`, `ja`, `ko`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`

Ubuntu Mono

`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`

Zen Maru Gothic

`bg`, `cs`, `el`, `hr`, `ko`, `lt`, `lv`, `pl`, `ro`, `ru`, `sk`, `th`, `vi`

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Apply branding](#branding "Apply branding")

[Branding with Connect](#branding-with-connect "Branding with Connect")

[Change your brand name](#change-your-brand-name "Change your brand name")

[Font compatibility](#font-compatibility "Font compatibility")

Prodotti utilizzati

[

Checkout





](/payments/checkout)

[

Elements





](/payments/elements)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/customization/appearance?payment-ui=embedded-components

 Customize appearance | Stripe Documentation     

[Skip to content](#main-content)

Customize the appearance

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fappearance)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustomization%2Fappearance)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

Customize the appearance

[Customize text and policies](/payments/checkout/customization/policies)

[Customize behavior](/payments/checkout/customization/behavior)

[Use your custom domain](/payments/checkout/custom-domains)

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

[Set up future payments](/payments/checkout/save-and-reuse "Learn how to save payment details and charge your customers later")

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

United States

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page[Customize look and feel](/payments/checkout/customization "Customize look and feel")

Customize appearance
====================

Customize your checkout page's colors, fonts, shapes, and more.
---------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

Customize the appearance of Stripe Elements to match the design of your site by passing the [appearance](/js/custom_checkout/react/checkout_provider#custom_checkout_react_checkout_provider-options-elementsOptions-appearance) prop to the `CheckoutProvider` component. The layout of each Element stays consistent, but you can modify colors, fonts, borders, padding, and more.

Select a languageReact

`const appearance = {   theme: 'stripe', }; <CheckoutProvider   stripe={stripe}   options={{     clientSecret,     elementsOptions: {       appearance,     },   }} > </CheckoutProvider>`

1.  **Start by picking a [theme](#theme)**.

Get up and running right away by picking the prebuilt theme that most closely resembles your website.

1.  **Customize the theme using [variables](#variables)** .

Set variables like `fontFamily` and `colorPrimary` to broadly customize components appearing throughout each Element.

1.  **If needed, fine-tune individual components and states using [rules](#rules)** .

For complete control, specify custom CSS properties for individual components appearing in the Element.

Themes
------

Start customizing Elements by picking from one of the following themes:

*   `stripe`
*   `night`
*   `flat`

`const appearance = {   theme: 'night' };`

Variables
---------

Set variables to affect the appearance of many components appearing throughout each Element.

The `variables` option works like [CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties). You can specify CSS values for each variable and reference other variables with the `var(--myVariable)` syntax. You can even inspect the resulting DOM using the DOM explorer in your browser.

`const appearance = {   theme: 'stripe',    variables: {     colorPrimary: '#0570de',     colorBackground: '#ffffff',     colorText: '#30313d',     colorDanger: '#df1b41',     fontFamily: 'Ideal Sans, system-ui, sans-serif',     spacingUnit: '2px',     borderRadius: '4px',     // See all possible variables below   } };`

### Commonly used variables

Variable

Description

`fontFamily`

The font family used throughout Elements. Elements supports custom fonts by passing the `fonts` option to [initCheckout](/js/custom_checkout/init#custom_checkout_init-options-elementsOptions-fonts) or [CheckoutProvider](/js/custom_checkout/react/checkout_provider#custom_checkout_react_checkout_provider-options-elementsOptions-fonts).

`fontSizeBase`

The font size that’s set on the root of the Element. By default, other font size variables such as `fontSizeXs` or `fontSizeSm` are scaled from this value using `rem` units. Make sure that you choose a font size of at least 16px for input fields on mobile.

`spacingUnit`

The base spacing unit that all other spacing is derived from. Increase or decrease this value to make your layout more or less spacious.

`borderRadius`

The border radius used for tabs, inputs, and other components in the Element.

`colorPrimary`

A primary color used throughout the Element. Set this to your primary brand color.

`colorBackground`

The color used for the background of inputs, tabs, and other components in the Element.

`colorText`

The default text color used in the Element.

`colorDanger`

A color used to indicate errors or destructive actions in the Element.

### Less commonly used variables

Variable

Description

`fontSmooth`

What text anti-aliasing settings to use in the Element. It can be `always`, `auto`, or `never`.

`fontVariantLigatures`

The [font-variant-ligatures](http://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-ligatures) setting of text in the Element.

`fontVariationSettings`

The [font-variation-settings](http://developer.mozilla.org/en-US/docs/Web/CSS/font-variation-settings) setting of text in the Element.

`fontWeightLight`

The font weight used for light text.

`fontWeightNormal`

The font weight used for normal text.

`fontWeightMedium`

The font weight used for medium text.

`fontWeightBold`

The font weight used for bold text.

`fontLineHeight`

The [line-height](http://developer.mozilla.org/en-US/docs/Web/CSS/line-height) setting of text in the Element.

`fontSizeXl`

The font size of extra-large text in the Element. By default this is scaled from `var(--fontSizeBase)` using `rem` units.

`fontSizeLg`

The font size of large text in the Element. By default this is scaled from `var(--fontSizeBase)` using `rem` units.

`fontSizeSm`

The font size of small text in the Element. By default this is scaled from `var(--fontSizeBase)` using `rem` units.

`fontSizeXs`

The font size of extra-small text in the Element. By default this is scaled from `var(--fontSizeBase)` using `rem` units.

`fontSize2Xs`

The font size of double-extra small text in the Element. By default this is scaled from `var(--fontSizeBase)` using `rem` units.

`fontSize3Xs`

The font size of triple-extra small text in the Element. By default this is scaled from `var(--fontSizeBase)` using `rem` units.

`logoColor`

A preference for which logo variations to display; either `light` or `dark`.

`tabLogoColor`

The logo variation to display inside `.Tab` components; either `light` or `dark`.

`tabLogoSelectedColor`

The logo variation to display inside the `.Tab--selected` component; either `light` or `dark`.

`blockLogoColor`

The logo variation to display inside `.Block` components; either `light` or `dark`.

`colorSuccess`

A color used to indicate positive actions or successful results in the Element.

`colorWarning`

A color used to indicate potentially destructive actions in the Element.

`accessibleColorOnColorPrimary`

The color of text appearing on top of any `var(--colorPrimary)` background.

`accessibleColorOnColorBackground`

The color of text appearing on top of any `var(--colorBackground)` background.

`accessibleColorOnColorSuccess`

The color of text appearing on top of any `var(--colorSuccess)` background.

`accessibleColorOnColorDanger`

The color of text appearing on top of any `var(--colorDanger)` background.

`accessibleColorOnColorWarning`

The color of text appearing on top of any `var(--colorWarning)` background.

`colorTextSecondary`

The color used for text of secondary importance. For example, this color is used for the label of a tab that isn’t currently selected.

`colorTextPlaceholder`

The color used for input placeholder text in the Element.

`iconColor`

The default color used for icons in the Element, such as the icon appearing in the card tab.

`iconHoverColor`

The color of icons when hovered.

`iconCardErrorColor`

The color of the card icon when it’s in an error state.

`iconCardCvcColor`

The color of the CVC variant of the card icon.

`iconCardCvcErrorColor`

The color of the CVC variant of the card icon when the CVC field has invalid input.

`iconCheckmarkColor`

The color of checkmarks displayed within components like `.Checkbox`.

`iconChevronDownColor`

The color of arrow icons displayed within select inputs.

`iconChevronDownHoverColor`

The color of arrow icons when hovered.

`iconCloseColor`

The color of close icons, used for indicating a dismissal or close action.

`iconCloseHoverColor`

The color of close icons when hovered.

`iconLoadingIndicatorColor`

The color of the spinner in loading indicators.

`iconMenuColor`

The color of menu icons used to indicate a set of additional actions.

`iconMenuHoverColor`

The color of menu icons when hovered.

`iconMenuOpenColor`

The color of menu icons when opened.

`iconPasscodeDeviceColor`

The color of the passcode device icon, used to indicate a message has been sent to the user’s mobile device.

`iconPasscodeDeviceHoverColor`

The color of the passcode device icon when hovered.

`iconPasscodeDeviceNotificationColor`

The color of the notification indicator displayed over the passcode device icon.

`iconRedirectColor`

The color of the redirect icon that appears for redirect-based payment methods.

`tabIconColor`

The color of icons appearing in a tab.

`tabIconHoverColor`

The color of icons appearing in a tab when the tab is hovered.

`tabIconSelectedColor`

The color of icons appearing in a tab when the tab is selected.

`tabIconMoreColor`

The color of the icon that appears in the trigger for the additional payment methods menu.

`tabIconMoreHoverColor`

The color of the icon that appears in the trigger for the additional payment methods menu when the trigger is hovered.

`accordionItemSpacing`

The vertical spacing between `.AccordionItem` components. This is only applicable when [spacedAccordionItems](/js/elements_object/create_payment_element#payment_element_create-options-layout-spacedAccordionItems) is `true`.

`gridColumnSpacing`

The spacing between columns in the grid used for the Element layout.

`gridRowSpacing`

The spacing between rows in the grid used for the Element layout.

`pickerItemSpacing`

The spacing between `.PickerItem` components rendered within the `.Picker` component.

`tabSpacing`

The horizontal spacing between `.Tab` components.

Rules
-----

The `rules` option is a map of CSS-like selectors to CSS properties, allowing granular customization of individual components. After defining your `theme` and `variables`, use `rules` to seamlessly integrate Elements to match the design of your site.

`const appearance = {     rules: {       '.Tab': {         border: '1px solid #E0E6EB',         boxShadow: '0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 6px rgba(18, 42, 66, 0.02)',       },        '.Tab:hover': {         color: 'var(--colorText)',       },        '.Tab--selected': {         borderColor: '#E0E6EB',         boxShadow: '0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 6px rgba(18, 42, 66, 0.02), 0 0 0 2px var(--colorPrimary)',       },        '.Input--invalid': {         boxShadow: '0 1px 1px 0 rgba(0, 0, 0, 0.07), 0 0 0 2px var(--colorDanger)',       },        // See all supported class names and selector syntax below     }   };`

### All rules

The selector for a rule can target any of the public class names in the Element, as well as the supported states, pseudo-classes, and pseudo-elements for each class. For example, the following are valid selectors:

*   `.Tab, .Label, .Input`
*   `.Tab:focus`
*   `.Input--invalid, .Label--invalid`
*   `.Input::placeholder`

The following are **not** valid selectors:

*   `.p-SomePrivateClass, img`, only public class names can be targeted
*   `.Tab .TabLabel`, ancestor-descendant relationships in selectors are unsupported
*   `.Tab--invalid`, the `.Tab` class does not support the `--invalid` state

Each class name used in a selector [supports an allowlist of CSS properties](#supported-css-properties), that you specify using camel case (for example, `boxShadow` for the [box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow) property).

The following is the complete list of supported class names and corresponding states, pseudo-classes, and pseudo-elements.

### Tabs

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesTabs@2x.9c36db7ee4c98d7b2d6f00e91e6d4f20.png)

Class name

States

Pseudo-classes

Pseudo-elements

`.Tab`

`--selected`

`:hover`, `:focus`, `:active`, `:disabled`

`.TabIcon`

`--selected`

`:hover`, `:focus`, `:active`, `:disabled`

`.TabLabel`

`--selected`

`:hover`, `:focus`, `:active`, `:disabled`

### Form Inputs - Labels Above

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesFormInputs@2x.4ed082ee74fcbad043a80e2d4b133b35.png)

Make sure that you choose a font size of at least 16px for input fields on mobile.

Class name

States

Pseudo-classes

Pseudo-elements

`.Label`

`--empty`, `--invalid`, `--focused`

`.Input`

`--empty`, `--invalid`

`:hover`, `:focus`, `:disabled`, `:autofill`

`::placeholder`, `::selection`

`.Error`

### Form Inputs - Floating Labels

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesFormInputsFloating@2x.daec4a823ac24cc86d94a44664104eb8.png)

#### Note

Floating Labels can be enabled as an [additional configuration option](#others).

Class name

States

Pseudo-classes

Pseudo-elements

`.Label`

`--empty`, `--invalid`, `--focused`, `--floating`, `--resting`

`.Input`

`--empty`, `--invalid`

`:hover`, `:focus`, `:disabled`, `:autofill`

`::placeholder`, `::selection`

`.Error`

### Block

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesBlock@2x.556532f7e919aaf1d775ceb0253f5c22.png)

Class name

States

Pseudo-classes

Pseudo-elements

`.Block`

`.BlockDivider`

`.BlockAction`

`--negative`

`:hover`, `:focus`, `:active`

### Code Input

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesCodeInput@2x.64975e4945d393068a2f207a2d48f25c.png)

Class name

States

Pseudo-classes

Pseudo-elements

`.CodeInput`

`:hover`, `:focus`, `:disabled`

### Checkbox

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesCheckbox@2x.d7bedd38a342344eb06d5bff5dd6ae43.png)

Class name

States

Pseudo-classes

Pseudo-elements

`.Checkbox`

`--checked`

`.CheckboxLabel`

`--checked`

`:hover`, `:focus`, `:focus-visible`

`.CheckboxInput`

`--checked`

`:hover`, `:focus`, `:focus-visible`

### Dropdown

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesDropdown@2x.d635e032d2a254d672c11825a2d3d23d.png)

Class name

States

Pseudo-classes

Pseudo-elements

`.Dropdown`

`.DropdownItem`

`--highlight`

`:active`

### Switch

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesSwitch@2x.a263ba8361af937d5228a35d18c63645.png)

Class name

States

Pseudo-classes

Pseudo-elements

`.Switch`

`--active`

`:hover`

`.SwitchControl`

`:hover`

### Picker

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesPicker@2x.aa78c665be0c7e33a62992c8e7e33014.png)

Class name

States

Pseudo-classes

Pseudo-elements

`.PickerItem`

`--selected`, `--highlight`, `--new`, `--disabled`

`:hover`, `:focus`, `:active`

`.PickerAction`

`:hover`, `:focus`, `:active`

Make sure your `.PickerItem` active state stands out amongst the other states.

![](https://b.stripecdn.com/docs-statics-srv/assets/uxTipPickerDo@2x.cc709dc96a8e99e6b020f53216d4d585.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/uxTipPickerDont@2x.b31bc4b51910a6eece59d44fa92c5b4d.png)

**DO**

Use a noticeable, high-contrast primary color, weight, and/or outline to distinguish the active state your customer has already selected.

**DON’T**

Don’t use two equally weighted options or low-contrast colors for your .PickerItem states because it makes distinguishing which one is active more difficult.

### Menu

Class name

States

Pseudo-classes

Pseudo-elements

`.Menu`

`.MenuIcon`

`--open`

`:hover`

`.MenuAction`

`--negative`

`:hover`, `:focus`, `:active`

### Accordion

Class name

States

Pseudo-classes

Pseudo-elements

`.AccordionItem`

`--selected`

`:hover`, `:focus-visible`

### Payment Method Messaging Element

Class name

States

Pseudo-classes

Pseudo-elements

`.PaymentMethodMessaging`

### Radio Icon

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesRadioIcon@2x.25886d6b352ac0a8d003e7e2cd39677d.png)

Class name

States

Pseudo-classes

Pseudo-elements

`.RadioIcon`

`.RadioIconOuter`

`--checked`, `--hovered`

`.RadioIconInner`

`--checked`, `--hovered`

You can control the overall size of the icon with the `width` property on `.RadioIcon`. You can control the relative size of `.RadioIconInner` with the `r` (radius) property. `.RadioIconOuter` and `.RadioIconInner` are SVG elements and can be styled with `stroke` and `fill` properties. See the full list of [supported CSS properties](#supported-css-properties) below.

`const appearance = {   rules: {     '.RadioIcon': {       width: '24px'     },     '.RadioIconOuter': {       stroke: '#E0E6EB'     },     '.RadioIconInner': {       r: '16'     }   } };`

### Supported CSS properties

CSS Property

Supported classes

`-moz-osx-font-smoothing`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`-webkit-font-smoothing`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`-webkit-text-fill-color`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`backgroundColor`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `BlockDivider`, `Button`, `CheckboxInput`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `InputDivider`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `Switch`, `Tab`, `ToggleItem`

`border`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderBottom`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderBottomColor`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderBottomLeftRadius`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderBottomRightRadius`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderBottomStyle`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderBottomWidth`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderColor`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderLeft`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderLeftColor`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderLeftStyle`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderLeftWidth`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderRadius`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `InputCloseIcon`, `Link`, `MenuAction`, `MenuIcon`, `PasscodeCloseIcon`, `PasscodeShowIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Switch`, `SwitchControl`, `Tab`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`borderRight`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderRightColor`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderRightStyle`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderRightWidth`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderStyle`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderTop`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderTopColor`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderTopLeftRadius`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderTopRightRadius`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderTopStyle`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderTopWidth`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`borderWidth`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Switch`, `SwitchControl`, `Tab`, `TermsText`, `Text`, `ToggleItem`

`boxShadow`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `InputCloseIcon`, `Link`, `MenuAction`, `MenuIcon`, `PasscodeCloseIcon`, `PasscodeShowIcon`, `PickerAction`, `PickerItem`, `SecondaryLink`, `Switch`, `SwitchControl`, `Tab`, `TermsLink`, `ToggleItem`

`color`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabIcon`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`fill`

`Action`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RadioIconInner`, `RadioIconOuter`, `SwitchControl`, `Tab`, `TabIcon`, `ToggleItem`

`fillOpacity`

`RadioIconInner`, `RadioIconOuter`

`fontFamily`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`fontSize`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Switch`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`fontVariant`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`fontWeight`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`letterSpacing`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`lineHeight`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`margin`

`Action`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `MenuAction`, `PickerAction`, `PickerItem`, `Tab`, `ToggleItem`

`marginBottom`

`Action`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `MenuAction`, `PickerAction`, `PickerItem`, `Tab`, `ToggleItem`

`marginLeft`

`Action`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `MenuAction`, `PickerAction`, `PickerItem`, `Tab`, `ToggleItem`

`marginRight`

`Action`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `MenuAction`, `PickerAction`, `PickerItem`, `Tab`, `ToggleItem`

`marginTop`

`Action`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `MenuAction`, `PickerAction`, `PickerItem`, `Tab`, `ToggleItem`

`opacity`

`Label`

`outline`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `InputCloseIcon`, `Link`, `MenuAction`, `MenuIcon`, `PasscodeCloseIcon`, `PasscodeShowIcon`, `PickerAction`, `PickerItem`, `SecondaryLink`, `Switch`, `SwitchControl`, `Tab`, `TermsLink`, `ToggleItem`

`outlineOffset`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Input`, `InputCloseIcon`, `Link`, `MenuAction`, `MenuIcon`, `PasscodeCloseIcon`, `PasscodeShowIcon`, `PickerAction`, `PickerItem`, `SecondaryLink`, `Switch`, `SwitchControl`, `Tab`, `TermsLink`, `ToggleItem`

`padding`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Menu`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Tab`, `TabIcon`, `TabLabel`, `TermsText`, `Text`, `ToggleItem`

`paddingBottom`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Menu`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Tab`, `TabIcon`, `TabLabel`, `TermsText`, `Text`, `ToggleItem`

`paddingLeft`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Menu`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Tab`, `TabIcon`, `TabLabel`, `TermsText`, `Text`, `ToggleItem`

`paddingRight`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Menu`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Tab`, `TabIcon`, `TabLabel`, `TermsText`, `Text`, `ToggleItem`

`paddingTop`

`AccordionItem`, `Action`, `Block`, `BlockAction`, `Button`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Menu`, `MenuAction`, `MenuIcon`, `PickerAction`, `PickerItem`, `RedirectText`, `Tab`, `TabIcon`, `TabLabel`, `TermsText`, `Text`, `ToggleItem`

`r`

`RadioIconInner`

`stroke`

`RadioIconInner`, `RadioIconOuter`

`strokeOpacity`

`RadioIconInner`, `RadioIconOuter`

`strokeWidth`

`RadioIconInner`, `RadioIconOuter`

`textAlign`

`PaymentMethodMessaging`

`textDecoration`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`textShadow`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`textTransform`

`AccordionItem`, `Action`, `BlockAction`, `Button`, `Checkbox`, `CheckboxLabel`, `CodeInput`, `DropdownItem`, `Error`, `Input`, `Label`, `Link`, `MenuAction`, `PickerAction`, `PickerItem`, `RedirectText`, `SecondaryLink`, `Tab`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`transition`

`Action`, `Block`, `BlockAction`, `Button`, `CheckboxInput`, `CheckboxLabel`, `CodeInput`, `Dropdown`, `DropdownItem`, `Error`, `Icon`, `Input`, `InputCloseIcon`, `Label`, `Link`, `MenuAction`, `MenuIcon`, `PasscodeCloseIcon`, `PasscodeShowIcon`, `PickerAction`, `PickerItem`, `RadioIconInner`, `RadioIconOuter`, `RedirectText`, `SecondaryLink`, `Switch`, `SwitchControl`, `Tab`, `TabIcon`, `TabLabel`, `TermsLink`, `TermsText`, `Text`, `ToggleItem`

`width`

`RadioIcon`

Some exceptions to the properties above are:

*   `-webkit-text-fill-color` isn’t compatible with pseudo-classes

Other configuration options
---------------------------

In addition to `themes`, `variables` and `rules`, we have provided additional appearance configuration options to style Elements.

You can customize these by adding them to the appearance object:

``const appearance = {   labels: 'floating',    // other configurations such as `theme`, `variables` and `rules`... }``

We currently support the below options:

Configuration

Description

`disableAnimations`

Disables animations throughout Elements. Boolean, defaults to `false`.

`labels`

Enables switching between labels above form fields and floating labels within the form fields; it can be either `above` or `floating`

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Themes](#theme "Themes")

[Variables](#variables "Variables")

[Commonly used variables](#commonly-used-variables "Commonly used variables")

[Rules](#rules "Rules")

[All rules](#all-rules "All rules")

[Tabs](#tabs "Tabs")

[Form Inputs - Labels Above](#form-inputs---labels-above "Form Inputs - Labels Above")

[Form Inputs - Floating Labels](#form-inputs---floating-labels "Form Inputs - Floating Labels")

[Block](#block "Block")

[Code Input](#code-input "Code Input")

[Checkbox](#checkbox "Checkbox")

[Dropdown](#dropdown "Dropdown")

[Switch](#switch "Switch")

[Picker](#picker "Picker")

[Menu](#menu "Menu")

[Accordion](#accordion "Accordion")

[Payment Method Messaging Element](#payment-method-messaging-element "Payment Method Messaging Element")

[Radio Icon](#radio-icon "Radio Icon")

[Other configuration options](#others "Other configuration options")

Products Used

[

Checkout





](/payments/checkout)

[

Elements





](/payments/elements)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=embedded-form

 How Checkout works | Stripe Documentation     

[Skip to content](#main-content)

How Checkout works

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

[Overview](/payments/checkout)

How Checkout works

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Netherlands

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Checkout

How Checkout works
==================

Learn how to use Checkout to collect payments on your website.
--------------------------------------------------------------

Checkout is a low-code payment integration that creates a customizable form for collecting payments.

Checkout’s built-in features allow you to reduce your development time. It supports 40+ payment methods, including [Link](/payments/link), which lets your customers save their payment method for faster checkout. You can accept payments by embedding Checkout directly into your website, redirecting customers to a Stripe-hosted payment page, or creating a customized checkout page with [Stripe Elements](/payments/elements). Checkout supports payments for both [one-time purchases](/payments/online-payments) and [subscriptions](/subscriptions).

You can also customize Checkout and access additional functionality with the [Checkout Sessions API](/api/checkout/sessions) and the Stripe Dashboard. For a complete list of features, see its [built-in and customizable features](/payments/checkout/how-checkout-works#features).

Stripe-hosted page

Embedded form

Embedded components

Public preview

Checkout lifecycle
------------------

1.  When a customer is ready to complete their purchase, your application creates a new Checkout Session.
2.  You mount Checkout as an embeddable component on your website to show a payment form.
3.  Customers enter their payment details and complete the transaction.
4.  After the transaction, the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) webhook event triggers the [order fulfillment process](/checkout/fulfillment).

Client

Server

Stripe API

Stripe Checkout

Send order information

Create Checkout Session

Return Checkout Session

checkout.session.created

Return Checkout Session client secret

Mount Checkout on your website

Customer completes payment

Customer returns to your website

Handle fulfillment

checkout.session.completed

A diagram of an embedded form integration's lifecycle

Low-code integration
--------------------

Checkout requires minimal coding and is the best choice for most integrations because of its prebuilt functionalities and customization options. You can integrate Checkout by creating a Checkout Session and collecting customer payment details. Collect payment by [embedding a payment form](/payments/accept-a-payment?platform=web&ui=embedded-form) in your website.

[Compare Checkout](/payments/online-payments#compare-features-and-availability) to other Stripe payment options to determine the best one for you. Checkout displays a payment form to collect customer payment information, validates cards, handles errors, and so on.

Built-in and customizable features
----------------------------------

Stripe Checkout has the following built-in and customizable features:

### Built-in features

*   Support for digital wallets and Link
*   Responsive mobile design
*   SCA-ready
*   CAPTCHAs
*   PCI compliance
*   Card validation
*   Error messaging
*   [Adjustable quantities](/payments/checkout/adjustable-quantity)
*   [Automatic tax collection](/tax/checkout)
*   International language support
*   [Adaptive Pricing](/payments/checkout/adaptive-pricing)

### Customizable features

*   [Collect taxes](/payments/checkout/taxes)
*   [Custom branding with colors, buttons, and font](/payments/checkout/customization)
*   [Cross-sells](/payments/checkout/cross-sells)
*   [Global payment methods](/payments/dashboard-payment-methods)
*   [Subscription upsells](/payments/checkout/upsells)
*   [Custom domains](/payments/checkout/custom-domains) (Stripe-hosted page only)
*   [Email receipts](/receipts)
*   [Apply discounts](/payments/checkout/discounts)
*   [Custom success page](/payments/checkout/custom-success-page)
*   [Recover abandoned carts](/payments/checkout/abandoned-carts)
*   [Autofill payment details with Link](/payments/checkout/customization/behavior#link)
*   [Collect Tax IDs](/tax/checkout/tax-ids)
*   [Collect shipping information](/payments/collect-addresses?payment-ui=checkout)
*   [Collect phone numbers](/payments/checkout/phone-numbers)
*   [Set the subscription billing cycle date](/payments/checkout/billing-cycle)

### Custom branding

You can set fonts, colors, icons, and field styles for your embedded form using the [Branding settings](https://dashboard.stripe.com/settings/branding/checkout) in the Dashboard. For more information, see [Customize your integration](/payments/checkout/customization).

Checkout Session
----------------

The Checkout Session is a programmatic representation of what your customers see on the payment form. After creating a Checkout Session, mount Checkout on your payment page to complete the purchase. When customers complete their purchase, you can [fulfill their orders](/checkout/fulfillment) by configuring an [event destination](/event-destinations) to process Checkout Session events. This code snippet from the [quickstart guide](/checkout/quickstart) is an example of how to create a Checkout Session in your application.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \  -d ui_mode=embedded \   --data-urlencode return_url="[https://example.com/return](https://example.com/return)"`

### One-time and recurring payments

Allow customers to make one-time payments or subscribe to a product or service by setting the [mode](/api/checkout/sessions/create#create_checkout_session-mode) parameter in a Checkout Session.

Mode

Purchase type

Payment

One-time purchases

[Subscription](/billing/subscriptions/overview)

*   Recurring purchases
*   Mixed cart: Recurring purchases with one-time purchases

### Mixed cart

Create a mixed cart in Checkout that lets your customers purchase Subscription items and one-time purchase items at the same time. To create a mixed cart, set the `mode` parameter to `subscription` and include the Price IDs, or `price_data`, for each line\_item in the [line\_items](/api/checkout/sessions/create#create_checkout_session-line_items) array. Price IDs come from Price objects created using the Stripe Dashboard or API and allow you to store information about your product catalog in Stripe.

You can also use [price\_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data) to reference information from an external database where you’re hosting price and product details without storing product catalog information on Stripe. For more information, see [Build a subscriptions integration](/billing/subscriptions/build-subscriptions).

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d "line_items[0][price]"={{RECURRING_PRICE_ID}} \   -d "line_items[0][quantity]"=1 \  -d "line_items[1][price]"={{ONE_TIME_PRICE_ID}} \   -d "line_items[1][quantity]"=1 \  -d mode=subscription \  -d ui_mode=embedded \   --data-urlencode return_url="https://example.com/return"`

### Payment methods

You can view, enable, and disable different payment methods in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) at any time. Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. View our [complete list of payment methods](/payments/payment-methods/overview).

### Save payment details and default payment methods

You can [save payment details for future use](/payments/save-and-reuse) by sending an API parameter when you create a Session. Options to save payment details include:

*   **Single payment**: If your Checkout Session uses `payment` mode, set the [payment\_intent\_data.setup\_future\_usage](/payments/payment-intents#future-usage) parameter.
*   **Subscription payment**: If your Checkout Session uses `subscription` mode, Stripe saves the payment method by default.
*   [Multiple saved payment methods](/payments/accept-a-payment?platform=web&ui=checkout#save-payment-method-details): If a customer has multiple payment methods saved, you can store a default payment method to the Customer object’s [default\_payment\_method](/api/customers/object#customer_object-invoice_settings-default_payment_method) field. However, these payment methods don’t appear for return purchases in Checkout.

### Guest customers

The `Customer` object represents a customer of your business, and it helps tracking subscriptions and payments that belong to the same customer. Checkout Sessions that don’t create Customers are associated with [guest customers](/payments/checkout/guest-customers) instead.

Complete a transaction
----------------------

To automate business flows after a transaction has occurred, register an [event destination](/event-destinations) and build a [webhook endpoint handler](/webhooks/quickstart). Consider the following events and automations to enable:

*   Process the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event to fullfill orders when a customer completes their purchase
*   Process the [checkout.session.expired](/api/events/types#event_types-checkout.session.expired) event to return items to your inventory or send users a cart [abandonment](/payments/checkout/abandoned-carts) email when they don’t make a purchase and their cart expires

See also
--------

*   [Checkout quickstart](/checkout/quickstart)
*   [Fulfill your orders](/checkout/fulfillment)
*   [Collect taxes in Checkout](/payments/checkout/taxes)
*   [Manage limited inventory with Checkout](/payments/checkout/managing-limited-inventory)
*   [Automatically convert to local currencies with Adaptive Pricing](/payments/checkout/adaptive-pricing)

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Checkout lifecycle](#lifecycle "Checkout lifecycle")

[Low-code integration](#low-code "Low-code integration")

[Built-in and customizable features](#features "Built-in and customizable features")

[Built-in features](#built-in "Built-in features")

[Customizable features](#customizable "Customizable features")

[Custom branding](#branding "Custom branding")

[Checkout Session](#session "Checkout Session")

[One-time and recurring payments](#checkout-mode "One-time and recurring payments")

[Mixed cart](#mixed-cart "Mixed cart")

[Payment methods](#payment-methods "Payment methods")

[Save payment details and default payment methods](#save-payment-methods "Save payment details and default payment methods")

[Guest customers](#guest-customers "Guest customers")

[Complete a transaction](#complete-transaction "Complete a transaction")

[See also](#see-also "See also")

Related Guides

[

No-code options to accept payments on Stripe



](/no-code)

[

Prebuilt checkout page



](/checkout/quickstart)

[

Learn about payment methods



](/payments/payment-methods/overview)

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/custom-shipping-options?oo-step=true&should-crawl=true&record-id=q4v76ci2vx&wait-before-scraping=2000&save-html=true&save-markdown=true

 Dynamically customize shipping options | Documentazione Stripe     

[Passa al contenuto](#main-content)

Personalizzare le opzioni di spedizione in modo dinamico

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-shipping-options)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-shipping-options)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

Personalizzare le opzioni di spedizione in modo dinamico

[Aggiornare le voci riga in modo dinamico](/payments/checkout/dynamically-update-line-items)

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

[Configura pagamenti futuri](/payments/checkout/save-and-reuse "Come salvare i dati di pagamento e addebitare i pagamenti ai clienti in seguito")

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page[Dynamically update checkout](/payments/checkout/dynamic-updates "Dynamically update checkout")

Dynamically customize shipping optionsAnteprima privata
=======================================================

Update shipping options based on a customer's shipping address.
---------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Dynamic updates aren’t available with Stripe-hosted pages.

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/save-and-reuse?oo-step=true&should-crawl=true&record-id=i49ns7nn4k&wait-before-scraping=2000&save-html=true&save-markdown=true

 Set up future payments | Stripe Documentation     

[Skip to content](#main-content)

Set up future payments

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fsave-and-reuse)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fsave-and-reuse)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

[Overview](/payments/checkout/build-integration "Build a payments experience with Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Start with sample code.")

[Customize look and feel](/payments/checkout/customization "Control the appearance of your checkout page. The level of customization depends on the product you use.")

[Collect additional information](/payments/checkout/collect-additional-info "Collect information like shipping addresses and phone numbers as part of the checkout process.")

[Collect taxes](/payments/checkout/taxes)

[Dynamically update checkout](/payments/checkout/dynamic-updates "Make updates while your customer checks out.")

[Manage your product catalog](/payments/checkout/product-catalog)

[Subscriptions](/payments/subscriptions "Manage subscriptions with Checkout")

[Manage payment methods](/payments/checkout/payment-methods)

[Let customers pay in their local currency](/payments/checkout/adaptive-pricing)

[Add discounts, upsells, and cross-sells](/payments/checkout/promotions)

Set up future payments

[Save payment details during payment](/payments/checkout/save-during-payment "Save payment details during payment")

[After the payment](/payments/checkout/after-the-payment)

[Elements with Checkout Sessions API changelog](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrate from legacy Checkout](/payments/checkout/migration)

[Migrate Checkout to use Prices](/payments/checkout/migrating-prices)

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Malaysia

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Build a checkout page

Set up future payments
======================

Learn how to save payment details and charge your customers later.
------------------------------------------------------------------

Stripe-hosted page

Embedded form

Embedded components

Public preview

To collect customer payment details that you can reuse later, use Checkout’s setup mode. Setup mode uses the [Setup Intents API](/api/setup_intents) to create [Payment Methods](/api/payment_methods).

Check out our [full, working sample on GitHub](https://github.com/stripe-samples/checkout-remember-me-with-twilio-verify).

[

Set up Stripe

Server-side




------------------------------





](#set-up-stripe)

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries to access the Stripe API from your application:

Command Line

Select a languageRuby

`# Available as a gem sudo gem install stripe`

Gemfile

Select a languageRuby

`# If you use bundler, you can add this line to your Gemfile gem 'stripe'`

[

Create a Checkout Session

Client-side

Server-side




-------------------------------------------------------





](#create-checkout-session)

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

index.html

`<html>   <head>     <title>Checkout</title>   </head>   <body>     <form action="/create-checkout-session" method="POST">       <button type="submit">Checkout</button>     </form>   </body> </html>`

To create a setup mode Session, use the `mode` parameter with a value of `setup` when creating the Session. You can optionally specify the [customer parameter](/api/checkout/sessions/create#create_checkout_session-customer) to automatically attach the created payment method to an existing customer. Checkout uses [Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods) by default, which requires you to pass the [currency](/api/checkout/sessions/create#create_checkout_session-currency) parameter when using `setup` mode.

Append the `{CHECKOUT_SESSION_ID}` template variable to the `success_url` to get access to the Session ID after your customer successfully completes a Checkout Session. After creating the Checkout Session, redirect your customer to the [URL](/api/checkout/sessions/object#checkout_session_object-url) returned in the response.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_CsnggH3iChIYjrFoue5y6M98  :" \  -d mode=setup \  -d currency=usd \  -d customer=  {{CUSTOMER_ID}}   \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})"`

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn individual payment methods on or off in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). By default, Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe filters them out even when they’re enabled. We filter Google Pay if you [enable automatic tax](/tax/checkout) without collecting a shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

[

Retrieve the Checkout Session

Server-side




----------------------------------------------





](#retrieve-checkout-session)

After a customer successfully completes their Checkout Session, you need to retrieve the Session object. There are two ways to do this:

*   **Asynchronously**: Handle `checkout.session.completed` [webhooks](/webhooks "webhook"), which contain a Session object. Learn more about [setting up webhooks](/webhooks).
*   **Synchronously**: Obtain the Session ID from the `success_url` when a user redirects back to your site. Use the Session ID to [retrieve](/api/checkout/sessions/retrieve) the Session object.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions/cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k \  -u "  sk_test_CsnggH3iChIYjrFoue5y6M98  :"`

The right choice depends on your tolerance for dropoff, as customers may not always reach the `success_url` after a successful payment. It’s possible for them close their browser tab before the redirect occurs. Handling webhooks prevents your integration from being susceptible to this form of dropoff.

After you have retrieved the Session object, get the value of the `setup_intent` key, which is the ID for the SetupIntent created during the Checkout Session. A [SetupIntent](/payments/setup-intents) is an object used to set up the customer’s bank account information for future payments.

Example `checkout.session.completed` payload:

`{   "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",   "object": "event",   "api_version": "2019-03-14",   "created": 1561420781,   "data": {     "object": {       "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",       "object": "checkout.session",       "billing_address_collection": null,       "client_reference_id": null,       "customer": "",       "customer_email": null,       "display_items": [],       "mode": "setup",       "setup_intent": "seti_1EzVO3HssDVaQm2PJjXHmLlM",       "submit_type": null,       "subscription": null,       "success_url": "[https://example.com/success](https://example.com/success)"     }   },   "livemode": false,   "pending_webhooks": 1,   "request": {     "id": null,     "idempotency_key": null   },   "type": "checkout.session.completed" }`

Note the `setup_intent` ID for the next step.

[

Retrieve the SetupIntent

Server-side




-----------------------------------------





](#retrieve-setup-intent)

Using the `setup_intent` ID, [retrieve](/api/setup_intents/retrieve) the SetupIntent object. The returned object contains a `payment_method` ID that you can attach to a customer in the next step.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/setup_intents/seti_1EzVO3HssDVaQm2PJjXHmLlM \  -u "  sk_test_CsnggH3iChIYjrFoue5y6M98  :"`

#### Note

If you’re requesting this information synchronously from the Stripe API (as opposed to handling webhooks), you can combine the previous step with this step by [expanding](/api/expanding_objects) the SetupIntent object in the request to the /v1/checkout/session endpoint. Doing this prevents you from having to make two network requests to access the newly created PaymentMethod ID.

[

Charge the payment method later

Server-side




------------------------------------------------





](#charge-saved-payment-method)

If you didn’t create the Checkout Session with an existing customer, use the ID of the PaymentMethod to [attach](/api/payment_methods/attach) the [PaymentMethod](/api/payment_methods "PaymentMethods") to a [Customer](/api/customers "Customers"). After you attach the PaymentMethod to a customer, you can make an off-session payment using a [PaymentIntent](/api/payment_intents/create#create_payment_intent-payment_method):

*   Set [customer](/api#create_payment_intent-customer) to the ID of the Customer and [payment\_method](/api#create_payment_intent-payment_method) to the ID of the PaymentMethod.
*   Set [off\_session](/api/payment_intents/confirm#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during a payment attempt and can’t fulfill an authentication request made by a partner, such as a card issuer, bank, or other payment institution. If, during your checkout flow, a partner requests authentication, Stripe requests exemptions using customer information from a previous on-session transaction. If the conditions for exemption aren’t met, the PaymentIntent might throw an error.
*   Set the value of the PaymentIntent’s [confirm](/api/payment_intents/create#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when you create the PaymentIntent.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/payment_intents \  -u "  sk_test_CsnggH3iChIYjrFoue5y6M98  :" \  -d amount=1099 \  -d currency=usd \  -d customer=  {{CUSTOMER_ID}}   \  -d payment_method=  {{PAYMENT_METHOD_ID}}   \  -d off_session=true \  -d confirm=true`

When a payment attempt fails, the request also fails with a 402 HTTP status code and the status of the PaymentIntent is [requires\_payment\_method](/upgrades#2019-02-11 "requires_payment_method"). Notify your customer to return to your application (for example, by sending an email or in-app notification) and direct your customer to a new Checkout Session to select another payment method.

Command Line

Select a languagecURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_CsnggH3iChIYjrFoue5y6M98  :" \  -d customer=  {{CUSTOMER_ID}}   \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][unit_amount]"=1099 \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})"`

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Set up Stripe](#set-up-stripe "Set up Stripe")

[Create a Checkout Session](#create-checkout-session "Create a Checkout Session")

[Payment methods](#payment-methods "Payment methods")

[Retrieve the Checkout Session](#retrieve-checkout-session "Retrieve the Checkout Session")

[Retrieve the SetupIntent](#retrieve-setup-intent "Retrieve the SetupIntent")

[Charge the payment method later](#charge-saved-payment-method "Charge the payment method later")

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/migration?oo-step=true&should-crawl=true&record-id=fdqmemcx39&wait-before-scraping=2000&save-html=true&save-markdown=true

 Migrationsleitfaden für Checkout | Stripe-Dokumentation     

[Weiter zum Inhalt](#main-content)

Bezahlseite erstellen

[

Konto erstellen



](https://dashboard.stripe.com/register)oder[

anmelden



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigration)

[

](/)

Die Dokumentation durchsuchen

/

[Konto erstellen](https://dashboard.stripe.com/register)

[

Anmelden



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigration)

[

Jetzt starten



](/get-started)

[

Zahlungen



](/payments)

[

Finanzautomatisierung



](/finance-automation)

[

Plattformen und Marktplätze



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Entwickler-Tools



](/development)

[

Jetzt starten



](/get-started)

[

Zahlungen



](/payments)

[

Finanzautomatisierung



](/finance-automation)

[

Jetzt starten



](/get-started)

[

Zahlungen



](/payments)

[

Finanzautomatisierung



](/finance-automation)

[

Plattformen und Marktplätze



](/connect)

[

Banking-as-a-Service



](/financial-services)

APIs und SDKs

Hilfe

[Übersicht](/payments)

Informationen zu Stripe Payments

[Aktualisieren Sie Ihre Integration](/payments/upgrades "Verbessern Sie Ihre bestehende Integration")

Zahlungsanalysefunktionen

Online-Zahlungen

[Übersicht](/payments/online-payments "Erfahren Sie mehr über Integrationsoptionen zur Annahme von Online-Zahlungen.")[Ihren Use case finden](/payments/use-cases/get-started "Erfahren Sie, wie Stripe Ihr Unternehmen unterstützen kann.")

Use Payment Links

Bezahlseite erstellen

[Übersicht](/payments/checkout/build-integration "Erstellen Sie eine Zahlungsoberfläche mit Checkout.")

[Quickstarts](/payments/checkout/quickstarts "Beginnen Sie mit Beispielcode.")

[Erscheinungsbild anpassen](/payments/checkout/customization "Bestimmen Sie das Erscheinungsbild Ihrer Checkout-Seite. Der Anpassungsgrad hängt vom verwendeten Produkt ab.")

[Zusätzliche Informationen erfassen](/payments/checkout/collect-additional-info "Erfassen Sie Informationen wie Versandadresse und Telefonnummern während des Bezahlvorgangs.")

[Steuern einziehen](/payments/checkout/taxes)

[Bezahlvorgang dynamisch aktualisieren](/payments/checkout/dynamic-updates "Führen Sie Updates durch, während Ihre Kundschaft bezahlt.")

[Ihren Produktkatalog verwalten](/payments/checkout/product-catalog)

[Abonnements](/payments/subscriptions "Abonnements mit Checkout verwalten")

[Zahlungsmethoden verwalten](/payments/checkout/payment-methods)

[Lassen Sie Kundinnen/Kunden in ihrer Landeswährung zahlen](/payments/checkout/adaptive-pricing)

[Rabatte, Upselling und Cross-Selling hinzufügen](/payments/checkout/promotions)

[Zukünftige Zahlungen einrichten](/payments/checkout/save-and-reuse "Erfahren Sie, wie Sie PayPal-Details speichern und die Konten Ihrer Kundinnen und Kunden später belasten")

[Zahlungsdaten bei der Zahlung speichern](/payments/checkout/save-during-payment "Zahlungsdaten bei der Zahlung speichern")

[Nach der Zahlung](/payments/checkout/after-the-payment)

[Elements mit Checkout Sessions API-Änderungsprotokoll](/checkout/elements-with-checkout-sessions-api/changelog)

Vom bisherigen Bezahlvorgang migrieren

[Bezahlvorgang auf Prices umstellen](/payments/checkout/migrating-prices)

Erweiterte Integration erstellen

In-App-Integration erstellen

Zahlungsmethoden

Zahlungsmethoden hinzufügen

Zahlungsmethoden verwalten

Schnellerer Bezahlvorgang mit Link

Nutzeroberflächen für Zahlungen

Payment Links

Checkout

Web Elements

In-App-Elements

Zahlungsszenarien

Nutzerdefinierte Zahlungsabläufe

Flexibles Acquiring

Präsenzzahlungen

Terminal

Andere Stripe-Produkte

Financial Connections

Krypto

Climate

Auszahlungs-Links

Deutschland

Deutsch

[Startseite](/ "Startseite")[Zahlungen](/payments "Zahlungen")Build a checkout page

Migrationsleitfaden für Checkout
================================

So migrieren Sie zu den neuesten Integrationen von Stripe.
----------------------------------------------------------

![](https://b.stripecdn.com/docs-statics-srv/assets/migration.4db0b4061fb36d6a43762c3f23ef9c00.png)

Die ältere Version von Checkout hat Kund/innen einen modalen Dialog präsentiert, der Karteninformationen erfasst und einen Token oder eine Quelle an Ihre Website zurückgegeben hat. Im Gegensatz dazu sind [Payment Links](/payment-links) und die aktuelle Version von [Checkout](/payments/checkout) intelligente, von Stripe gehostete Zahlungsseiten, die Zahlungen oder [Abonnements](/billing/subscriptions/creating "Abonnements") erstellen. Beide Integrationen unterstützen Apple Pay, Google Pay, dynamisches [3D Secure](/payments/3d-secure "3D Secure (3DS)"), [Connect](/connect "Connect"), die Wiederverwendung bestehender [Kunden/Kundinnen](/api/customers "Kund/innen") und viele andere Funktionen. Sie können auch [andere Zahlungsintegrationen vergleichen](/payments/online-payments#compare-features-and-availability), wenn Payment Links oder Checkout nicht zu Ihrem Anwendungsszenario passen.

Bevor Sie loslegen
------------------

Wenn Sie die [SDKs](/sdks) von Stripe verwenden, führen Sie ein Upgrade auf die neueste Version durch.

Wählen Sie Ihr Geschäftsmodell
------------------------------

Um von der älteren Version von Checkout auf die aktuelle umzustellen, folgen Sie dem Leitfaden, der Ihr Geschäftsmodell am ehesten repräsentiert. Jeder Leitfaden empfiehlt einen Integrationspfad mit einem Beispielcode.

*   [Dynamischer Produktkatalog und Preise](#api-products)
    
    Wenn Sie einen großen Produktkatalog haben oder Unterstützung für dynamisch generierte Einzelposten (wie Spenden oder Steuern) benötigen.
    
*   [Dynamische Abonnements](#api-subscriptions)
    
    Wenn Sie ein SaaS-Anbieter sind, der Nutzer/innen abrechnet und Unterstützung bei erweiterten Funktionen benötigen.
    
*   [Connect-Plattformen und -Marktplätze](#connect)
    
    Wenn Sie einen Marktplatz betreiben, auf dem Sie Dienstanbieter und Kund/innen miteinander vernetzen.
    
*   [Zahlungsmethoden für spätere Verwendung speichern](#setup-mode)
    
    Wenn Sie ein Unternehmen betreiben, das die Kund/innen erst abrechnet, wenn die Dienstleistung ausgeführt wurde.
    
*   [Einfacher Produktkatalog mit festen Preisen](#simple-products)
    
    Wenn Sie einige Produkte mit vorab bestimmten Preisen verkaufen.
    
*   [Einfache Abonnements](#simple-subscriptions)
    
    Wenn Sie ein SaaS-Anbieter mit monatlichem Abonnementplan sind.
    

Wenn Sie den entsprechenden Migrationsleitfaden befolgen, können Sie auch auf die [Konversionstabelle](#parameter-conversion) verweisen, um eine Zuordnung bestimmter Parameter und Konfigurationsoptionen zu erhalten.

Dynamischer Produktkatalog und Preise
-------------------------------------

Wenn Sie Produkte verkaufen, für die der Betrag oder die Einzelposten dynamisch festgelegt werden (z. B. bei einem großen Produktkatalog oder für Spenden), lesen Sie [Annahme von Einmalzahlungen](/payments/accept-a-payment?integration=checkout).

Möglicherweise haben Sie mit der älteren Checkout-Version einen Token oder eine Quelle auf dem Client erstellt und diese/n für spätere Nutzung an Ihren Server übergeben. Die aktuelle Version von Checkout kehrt diesen Vorgang jedoch um. Sie müssen zunächst eine Session auf Ihrem Server erstellen und dann Ihren Kunden/Ihre Kundin an Checkout weiterleiten, der/die nach der Zahlung wieder zu Ihrer Anwendung zurückgeleitet wird.

### Vor

Mit der älteren Version von Checkout würden Sie den dynamischen Betrag und die Beschreibung anzeigen und Karteninformationen von Ihrem Kunden/Ihrer Kundin erfassen.

client.html

`<form action="/purchase" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_f3duw0VsAEM2TJFMtWQ90QAT"      data-name="Custom t-shirt"     data-description="Your custom designed t-shirt"     data-amount="{{ORDER_AMOUNT}}"     data-currency="usd">   </script> </form>`

Als Nächstes würden Sie den resultierenden Token oder die Quelle an Ihren Server senden und abrechnen.

Command Line

Curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "email"="customer@example.com" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/charges \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "description"="Custom t-shirt" \   -d "amount"="{{ORDER_AMOUNT}}" \   -d "currency"="usd"`

### Nach

Fügen Sie Ihrer Website eine Schaltfläche zum Bezahlen hinzu, über die ein serverseitiger Endpoint aufgerufen wird, um eine [Checkout-Sitzung](/api/checkout/sessions/create) zu erstellen.

checkout.html

`<html>   <head>     <title>Buy cool new product</title>   </head>   <body>     <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->     <form action="/create-checkout-session" method="POST">       <button type="submit">Checkout</button>     </form>   </body> </html>`

Eine Checkout-Sitzung ist eine programmgesteuerte Darstellung dessen, was Ihren Kundinnen und Kunden bei der Weiterleitung zum Zahlungsformular angezeigt wird. Es gibt folgende Konfigurationsoptionen:

*   [Posten](/api/checkout/sessions/create#create_checkout_session-line_items) für die Zahlungsabwicklung
*   Zu verwendende Währungen

Fügen Sie eine `success_url` mit der URL einer Seite auf Ihrer Website ein, an die Ihre Kundinnen/Kunden nach Abschluss der Zahlung weitergeleitet werden.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  :" \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][price_data][product_data][name]"="Custom t-shirt" \  -d "line_items[0][price_data][unit_amount]"=2000 \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

Leiten Sie Ihre Kundinnen und Kunden nach dem Erstellen einer Checkout-Sitzung zu der in der Antwort zurückgegebenen [URL](/api/checkout/sessions/object#checkout_session_object-url) weiter. Wenn Sie gekaufte Waren nach der Zahlung abwickeln müssen, lesen Sie [Zahlungen per Checkout und Payment Link abwickeln](/checkout/fulfillment).

Dynamische Abonnements
----------------------

Wenn Sie Abonnementdienste anbieten, die dynamisch festgelegt werden oder Support für andere erweiterte Funktionen benötigen, finden Sie weitere Informationen unter [Einrichten eines Abonnements](/billing/subscriptions/build-subscriptions).

Möglicherweise haben Sie mit der älteren Checkout-Version einen Token oder eine Quelle auf dem Client erstellt und diese/n an Ihren Server übergeben, um einen Kunden/eine Kundin oder ein Abonnement zu erstellen. Die aktuelle Version von Checkout kehrt diesen Vorgang jedoch um. Sie müssen zunächst eine Sitzung auf Ihrem Server erstellen und dann Ihren Kunden/Ihre Kundin an Checkout weiterleiten, der/die bei Erfolg wieder zu Ihrer Anwendung zurückgeleitet wird.

### Vor

Mit der älteren Version von Checkout würden Sie die Abonnementinformationen anzeigen und Karteninformationen von Ihrem Kunden/Ihrer Kundin erfassen.

client.html

`<form action="/subscribe" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_f3duw0VsAEM2TJFMtWQ90QAT"      data-name="Gold Tier"     data-description="Monthly subscription with 30 days trial"     data-amount="2000"     data-label="Subscribe">   </script> </form>`

Als Nächstes würden Sie den resultierenden Token oder die Quelle an Ihren Server senden, um einen Kunden/eine Kundin und ein Abonnement zu erstellen.

Command Line

Curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "email"="customer@example.com" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/subscriptions \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "items[0][price]"="{PRICE_ID}" \   -d "trial_period_days"=30`

### Nach

Fügen Sie Ihrer Website eine Schaltfläche zum Bezahlen hinzu, über die ein serverseitiger Endpoint aufgerufen wird, um eine [Checkout-Sitzung](/api/checkout/sessions/create) zu erstellen.

checkout.html

`<html>   <head>     <title>Subscribe to cool new service</title>   </head>   <body>     <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->     <form action="/create-checkout-session" method="POST">       <button type="submit">Subscribe</button>     </form>   </body> </html>`

Eine Checkout-Sitzung ist eine programmgesteuerte Darstellung dessen, was Ihren Kundinnen und Kunden bei der Weiterleitung zum Zahlungsformular angezeigt wird. Es gibt folgende Konfigurationsoptionen:

*   [Posten](/api/checkout/sessions/create#create_checkout_session-line_items) für die Zahlungsabwicklung
*   Zu verwendende Währungen

Fügen Sie eine `success_url` mit der URL einer Seite auf Ihrer Website ein, an die Ihre Kundinnen/Kunden nach Abschluss der Zahlung weitergeleitet werden.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d "subscription_data[trial_period_days]"=30 \  -d mode=subscription \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

Leiten Sie Ihre Kundinnen und Kunden nach dem Erstellen einer Checkout-Sitzung zu der in der Antwort zurückgegebenen [URL](/api/checkout/sessions/object#checkout_session_object-url) weiter. Der Kunde/die Kundin wird zur `success_url` weitergeleitet, nachdem der Kunde/die Kundin und das Abonnement erstellt wurden. Wenn Sie gekaufte Dienstleistungen nach der Zahlung erbringen müssen, lesen Sie [Zahlungen per Checkout und Payment Link abwickeln](/checkout/fulfillment).

Connect-Plattformen und -Marktplätze
------------------------------------

Wenn Sie eine Connect-Plattform oder einen Connect-Marktplatz betreiben und Zahlungen mit verbundenen Konten erstellen, sollten Sie die aktuelle Version von Checkout verwenden.

Das folgende Beispiel zeigt, wie Sie die Checkout Sessions API verwenden, um eine Direct Charge zu verarbeiten. Sie können Checkout und Connect auch mit [Destination Charges](/connect/destination-charges?platform=web&ui=stripe-hosted) und [separaten Zahlungen und Überweisungen](/connect/separate-charges-and-transfers?platform=web&ui=stripe-hosted) verwenden.

### Vor

Mit der älteren Version von Checkout würden Sie Karteninformationen von Ihrem Kunden/Ihrer Kundin auf dem Client erfassen.

client.html

`<form action="/purchase" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_f3duw0VsAEM2TJFMtWQ90QAT"      data-name="Food Marketplace"     data-description="10 cucumbers from Roger's Farm"     data-amount="2000">   </script> </form>`

Als Nächstes würden Sie den resultierenden Token oder die Quelle an Ihren Server senden und im Namen des verbundenen Kontos abrechnen.

Command Line

Curl

`curl https://api.stripe.com/v1/charges \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "source"="{{TOKEN_ID}}" \   -d "description"="10 cucumbers from Roger\"s Farm" \   -d "amount"=2000 \   -d "currency"="usd" \   -d "application_fee_amount"=200 \   -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}"`

### Nach

Fügen Sie Ihrer Website eine Schaltfläche zum Bezahlen hinzu, über die ein serverseitiger Endpoint aufgerufen wird, um eine [Checkout-Sitzung](/api/checkout/sessions/create) zu erstellen.

checkout.html

`<html>   <head>     <title>Roger's Farm</title>   </head>   <body>     <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->     <form action="/create-checkout-session" method="POST">       <button type="submit">Checkout</button>     </form>   </body> </html>`

Eine Checkout-Sitzung ist eine programmgesteuerte Darstellung dessen, was Ihren Kundinnen und Kunden bei der Weiterleitung zum Zahlungsformular angezeigt wird. Es gibt folgende Konfigurationsoptionen:

*   [Posten](/api/checkout/sessions/create#create_checkout_session-line_items) für die Zahlungsabwicklung
*   Zu verwendende Währungen

Fügen Sie eine `success_url` mit der URL einer Seite auf Ihrer Website ein, an die Ihre Kundinnen/Kunden nach Abschluss der Zahlung weitergeleitet werden.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  :" \  -H "Stripe-Account:   {{CONNECTED_ACCOUNT_ID}}  " \  -d "line_items[0][price_data][currency]"=usd \   --data-urlencode "line_items[0][price_data][product_data][name]"="Cucumbers from Roger's Farm" \  -d "line_items[0][price_data][unit_amount]"=200 \  -d "line_items[0][quantity]"=10 \  -d "payment_intent_data[application_fee_amount]"=200 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success](https://example.com/success)"`

Leiten Sie Ihre Kundinnen und Kunden nach dem Erstellen einer Checkout-Sitzung zu der in der Antwort zurückgegebenen [URL](/api/checkout/sessions/object#checkout_session_object-url) weiter. Wenn Sie gekaufte Waren oder Dienstleistungen nach der Zahlung abwickeln bzw. erbringen müssen, lesen Sie [Zahlungen per Checkout und Payment Link abwickeln](/checkout/fulfillment).

Zahlungsmethoden für spätere Verwendung speichern
-------------------------------------------------

Wenn Sie Dienstleistungen anbieten, bei denen Kundinnen/Kunden nicht sofort abgerechnet werden, lesen Sie den Abschnitt [Einrichten zukünftiger Zahlungen](/payments/save-and-reuse?platform=checkout).

Möglicherweise haben Sie mit der älteren Checkout-Version einen Token oder eine Quelle auf dem Client erstellt und diese/n an Ihren Server übergeben, um ihn für spätere Verwendung zu speichern. Die aktuelle Version von Checkout kehrt diesen Vorgang jedoch um. Sie müssen zunächst eine Sitzung auf Ihrem Server erstellen und dann Ihren Kunden/Ihre Kundin an Checkout weiterleiten, der/die bei Erfolg wieder zu Ihrer Anwendung zurückgeleitet wird.

### Vor

Mit der älteren Version von Checkout würden Sie die Zahlungsinformationen anzeigen und Karteninformationen von Ihrem Kunden/Ihrer Kundin erfassen.

client.html

`<form action="/subscribe" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_f3duw0VsAEM2TJFMtWQ90QAT"      data-name="Cleaning Service"     data-description="Charged after your home is spotless"     data-amount="2000">   </script> </form>`

Als Nächstes würden Sie den resultierenden Token oder die Quelle an Ihren Server senden, um schließlich eine Zahlung zu erstellen.

Command Line

Curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "email"="customer@example.com" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/charges \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "description"="Cleaning service" \   -d "amount"="{{ORDER_AMOUNT}}" \   -d "currency"="usd"`

### Nach

Fügen Sie Ihrer Website eine Schaltfläche zum Bezahlen hinzu, über die ein serverseitiger Endpoint aufgerufen wird, um eine [Checkout-Sitzung](/api/checkout/sessions/create) zu erstellen.

checkout.html

`<html>   <head>     <title>Cleaning service</title>   </head>   <body>     <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->     <form action="/create-checkout-session" method="POST">       <button type="submit">Subscribe</button>     </form>   </body> </html>`

Eine Checkout-Sitzung ist eine programmgesteuerte Darstellung dessen, was Ihren Kundinnen und Kunden bei der Weiterleitung zum Zahlungsformular angezeigt wird. Es gibt folgende Konfigurationsoptionen:

*   [Posten](/api/checkout/sessions/create#create_checkout_session-line_items) für die Zahlungsabwicklung
*   Zu verwendende Währungen

Fügen Sie eine `success_url` mit der URL einer Seite auf Ihrer Website ein, an die Ihre Kundinnen/Kunden nach Abschluss der Zahlungseinrichtung weitergeleitet werden.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  :" \  -d mode=setup \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})"`

Leiten Sie Ihre Kundinnen und Kunden nach dem Erstellen einer Checkout-Sitzung zu der in der Antwort zurückgegebenen [URL](/api/checkout/sessions/object#checkout_session_object-url) weiter, um Details zu Zahlungsmethoden zu sammeln. Der Kunde/die Kundin wird nach Abschluss des Vorgangs zur `success_url` weitergeleitet. Wenn Sie bereit sind, eine Zahlung einzuziehen, [rufen Sie den SetupIntent](/payments/checkout/save-and-reuse?payment-ui=stripe-hosted#retrieve-checkout-session) aus der Checkout-Sitzung ab und bereiten Sie damit die Transaktion vor.

Einfacher Produktkatalog mit festen Preisen
-------------------------------------------

Wenn Sie Produkte mit festen Preisen (wie T-Shirts oder E-Books) verkaufen, lesen Sie den Leitfaden zu [Zahlungslinks](/payment-links/create). Möglicherweise haben Sie die ältere Version von Checkout verwendet, um ein Token oder eine Quelle auf dem Client zu erstellen, und diese dann an Ihren Server übergeben, um eine Zahlung zu erstellen.

### Vor

Mit der älteren Version von Checkout würden Sie den Betrag und die Beschreibung anzeigen und Karteninformationen von Ihrem Kunden/Ihrer Kundin erfassen.

client.html

`<form action="/pay" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_f3duw0VsAEM2TJFMtWQ90QAT"      data-name="T-shirt"     data-description="Comfortable cotton t-shirt"     data-amount="500"     data-currency="usd">   </script> </form>`

Als Nächstes würden Sie den resultierenden Token oder die Quelle an Ihren Server senden, um einen Kunden/eine Kundin und eine Zahlung zu erstellen.

Command Line

Curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "email"="{{STRIPE_EMAIL}}" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/charges \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "description"="T-shirt" \   -d "amount"=500 \   -d "currency"="usd"`

### Nach

Erstellen Sie ein [Produkt](/api/products) und einen [Preis](/api/prices), um den Artikel darzustellen. Im folgenden Beispiel wird das Produkt inline erstellt. Sie können diese Objekte auch im [Dashboard](https://dashboard.stripe.com/test/products) erstellen.

Command Line

cURL

`curl https://api.stripe.com/v1/prices \  -u "  sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  :" \  -d currency=usd \  -d unit_amount=500 \  -d "product_data[name]"=T-shirt`

Erstellen Sie im Dashboard mit dem Produkt und dem Preis einen [Payment Link](https://dashboard.stripe.com/payment-links/create). Klicken Sie nach dem Erstellen des Links auf die **Schaltfläche „Kaufen“**, um das Design zu konfigurieren und den Code zu generieren, den Sie kopieren und in Ihre Website einfügen können.

index.html

HTML

`<body>   <h1>Purchase your new kit</h1>   <!-- Paste your embed code script here. -->   <script     async     src="[https://js.stripe.com/v3/buy-button.js](https://js.stripe.com/v3/buy-button.js)">   </script>   <stripe-buy-button     buy-button-id=  '{{BUY_BUTTON_ID}}'      publishable-key=  "pk_test_f3duw0VsAEM2TJFMtWQ90QAT"    >   </stripe-buy-button> </body>`

Einfache Abonnements
--------------------

Wenn Sie einen einfachen Abonnementdienst anbieten (wie monatlichen Zugriff auf eine Software), lesen Sie den Leitfaden zu [Zahlungslinks](/payment-links/create). Möglicherweise haben Sie die ältere Version von Checkout verwendet, um ein Token oder eine Quelle auf dem Client zu erstellen, und diese dann an Ihren Server übergeben, um eine Kundin/einen Kunden und ein Abonnement zu erstellen.

### Vor

Mit der älteren Version von Checkout würden Sie die Abonnementinformationen anzeigen und Karteninformationen von Ihrem Kunden/Ihrer Kundin erfassen.

client.html

`<form action="/subscribe" method="POST">   <script     src="[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)"     class="stripe-button"     data-key=  "pk_test_f3duw0VsAEM2TJFMtWQ90QAT"      data-name="Gold Tier"     data-description="Monthly subscription"     data-amount="2000"     data-currency="usd"     data-label="Subscribe">   </script> </form>`

Als Nächstes würden Sie den resultierenden Token oder die Quelle an Ihren Server senden, um einen Kunden/eine Kundin und ein Abonnement zu erstellen.

Command Line

Curl

`curl https://api.stripe.com/v1/customers \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "email"="{{STRIPE_EMAIL}}" \   -d "source"="{{STRIPE_TOKEN}}" curl https://api.stripe.com/v1/subscriptions \   -u sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  : \   -d "customer"="{{CUSTOMER_ID}}" \   -d "items[][price]"="{PRICE_ID}" \   -d "items[][quantity]"=1`

### Nach

Erstellen Sie ein [Produkt](/api/products) und einen [Preis](/api/prices), um das Abonnement darzustellen. Im folgenden Beispiel wird das Produkt inline erstellt. Sie können diese Objekte auch im [Dashboard](https://dashboard.stripe.com/test/products) erstellen.

Command Line

cURL

`curl https://api.stripe.com/v1/prices \  -u "  sk_test_Y17KokhC3SRYCQTLYiU5ZCD2  :" \  -d currency=usd \  -d unit_amount=2000 \  -d "recurring[interval]"=month \  -d "product_data[name]"="Gold Tier"`

Erstellen Sie im Dashboard mit dem Produkt und dem Preis einen [Payment Link](https://dashboard.stripe.com/payment-links/create). Klicken Sie nach dem Erstellen des Links auf die **Schaltfläche „Kaufen“**, um das Design zu konfigurieren und den Code zu generieren, den Sie kopieren und in Ihre Website einfügen können.

index.html

HTML

`<body>   <h1>Purchase your new kit</h1>   <!-- Paste your embed code script here. -->   <script     async     src="[https://js.stripe.com/v3/buy-button.js](https://js.stripe.com/v3/buy-button.js)">   </script>   <stripe-buy-button     buy-button-id=  '{{BUY_BUTTON_ID}}'      publishable-key=  "pk_test_f3duw0VsAEM2TJFMtWQ90QAT"    >   </stripe-buy-button> </body>`

Parameter-Konversion
--------------------

Die aktuelle Version von Checkout unterstützt die meisten Funktionen der älteren Version. Sie verwenden jedoch nicht dieselbe API. Die folgende Tabelle ordnet die Parameter und Konfigurationsoptionen zwischen der Legacy-Version und der aktuellen Version zu. Eine vollständige Liste der Konfigurationsoptionen finden Sie unter [Checkout-Sitzungen](/api/checkout/sessions).

Ältere Version

Aktuelle Version

Tipps für die Integration

`allowRememberMe`

Nicht unterstützt

Sie können bestehende Kunden/Kundinnen durch Angabe des `customer`\-Parameters beim Erstellen einer [Checkout-Sitzung](/api/checkout/sessions/create) wiederverwenden. Sie können [Link](/payments/link/checkout-link) auch aktivieren, damit Ihre Kunden/Kundinnen ihre Zahlungsinformationen sicher speichern und wiederverwenden können.

`amount`

Automatisch als Summe der Beträge über alle `line_items` hinweg berechnet

Der Gesamtbetrag ist die Summe der Einzelposten, die Sie an Checkout übergeben.

`billingAddress`

`Session.billing_address_collection`

Checkout erfasst die Rechnungsadresse automatisch, wenn dies zur Betrugsprävention oder für aufsichtsbehördliche Zwecke erforderlich ist. Setzen Sie diesen Parameter auf `required`, um immer die Rechnungsadresse zu erfassen.

`closed`

`cancel_url`

Wenn ein/e Kund/in Checkout schließen möchte, kann er/sie entweder die Registerkarte im Browser schließen oder zur `cancel_url` navigieren.

`currency`

`Session.currency`

`description`

`Session.line_items.description` oder `product.description`

Wenn Sie einen Preis angeben, zeigt Checkout eine automatisch berechnete Beschreibung der Häufigkeit Ihrer Zahlungen an. Wenn Sie `Session.line_items` angeben, zeigt Checkout für jeden Einzelposten den `name` an.

`email`

`Session.customer_email`

Wenn Sie die E-Mail-Adresse Ihres Kunden/Ihrer Kundin bereits kennen, können Sie sie beim Erstellen der Checkout-Sitzung mit [customer\_email](/api/checkout/sessions/create#create_checkout_session-customer_email) vorausfüllen.

`image`

**Unternehmens-Branding**: Laden Sie Ihr Unternehmenslogo oder -symbol im Dashboard hoch.

**Produktbilder**: Geben Sie mit `product.images` Bilder für jeden Einzelposten an

Checkout verwendet bestimmte Bilder für das [Branding](/payments/checkout/customization/appearance#branding) Ihres Unternehmens und für die Produkte, die Sie verkaufen. Checkout zeigt standardmäßig Ihr Unternehmenslogo an und greift neben dem Namen Ihres Unternehmens auf das Symbol zurück.

`key`

Nicht länger ein an Checkout übergebener Parameter

`locale`

`Session.locale`

Sie können beim Erstellen einer Checkout-Sitzung einen unterstützten [Standort](/payments/checkout/customization/behavior#localization) angeben.

`name`

`product.name` für Preise, die in `Session.line_items` angegeben sind

Wenn Sie einen Preis angeben, zeigt Checkout dem Kunden/der Kundin den Namen des Produkts an, zu dem der Preis gehört. Wenn Sie `Session.line_items` angeben, zeigt Checkout für jeden Einzelposten den `name` an.

`panelLabel`

`submit_type`

Checkout passt den Schaltflächentext automatisch an die Artikel an, die Sie verkaufen. Verwenden Sie für Einmalzahlungen [submit\_type](/payments/checkout/customization/behavior#submit-button), um den Schaltflächentext anzupassen.

`shippingAddress`

`session.shipping_address_collection`

[Erfassen Sie Versandadressinformationen](/payments/collect-addresses?payment-ui=checkout), indem Sie ein Array von `allowed_countries` übergeben, in die Sie liefern möchten.

`token` oder `source`

`success_url`

In JavaScript gibt es nach abgeschlossener Zahlung keinen Rückruf mehr. Da Ihr/e Kund/in auf einer anderen Seite zahlt, richten Sie `success_url` so ein, dass er/sie nach Abschluss der Zahlung umgeleitet wird.

`zipCode`

Automatisch von Checkout erfasst

Checkout erfasst die Postleitzahl automatisch, wenn dies zur Betrugsprävention oder für aufsichtsbehördliche Zwecke erforderlich ist.

Siehe auch
----------

*   [Weitere Zahlungsmethoden hinzufügen](/payments/payment-methods/overview)
*   [Adressen und Telefonnummern erfassen](/payments/collect-addresses)

War diese Seite hilfreich?

JaNein

Benötigen Sie Hilfe? [Kontaktieren Sie den Kundensupport](https://support.stripe.com/).

Nehmen Sie an unserem [Programm für frühzeitigen Zugriff](https://insiders.stripe.dev/) teil.

Schauen Sie sich unseren [Produkt-Changelog](https://stripe.com/blog/changelog) an.

Fragen? [Sales-Team kontaktieren](https://stripe.com/contact/sales).

Unterstützt von [Markdoc](https://markdoc.dev)

Für Entwickler-Updates anmelden:

Anmelden

Sie können sich jederzeit abmelden. Lesen Sie unsere [Datenschutzerklärung](https://stripe.com/privacy).

Auf dieser Seite

[Bevor Sie loslegen](#before-you-begin "Bevor Sie loslegen")

[Wählen Sie Ihr Geschäftsmodell](#choose-your-business-model "Wählen Sie Ihr Geschäftsmodell")

[Dynamischer Produktkatalog und Preise](#api-products "Dynamischer Produktkatalog und Preise")

[Vor](#api-products-before "Vor")

[Nach](#api-products-after "Nach")

[Dynamische Abonnements](#api-subscriptions "Dynamische Abonnements")

[Vor](#api-subscriptions-before "Vor")

[Nach](#api-subscriptions-after "Nach")

[Connect-Plattformen und -Marktplätze](#connect "Connect-Plattformen und -Marktplätze")

[Vor](#connect-before "Vor")

[Nach](#connect-after "Nach")

[Zahlungsmethoden für spätere Verwendung speichern](#setup-mode "Zahlungsmethoden für spätere Verwendung speichern")

[Vor](#setup-mode--before "Vor")

[Nach](#setup-mode--after "Nach")

[Einfacher Produktkatalog mit festen Preisen](#simple-products "Einfacher Produktkatalog mit festen Preisen")

[Vor](#simple-products-before "Vor")

[Nach](#simple-products-after "Nach")

[Einfache Abonnements](#simple-subscriptions "Einfache Abonnements")

[Vor](#simple-subscriptions-before "Vor")

[Nach](#simple-subscriptions-after "Nach")

[Parameter-Konversion](#parameter-conversion "Parameter-Konversion")

[Siehe auch](#see-also "Siehe auch")

Verwendete Produkte

[

Checkout





](/payments/checkout)

[

Payment Links





](/payments/payment-links)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

Stripe Shell wurde für die Verwendung am Desktop konzipiert.

    $

---

## URL: https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=stripe-hosted

 Set up future payments | Documentazione Stripe     

[Passa al contenuto](#main-content)

Configura pagamenti futuri

[

Crea account



](https://dashboard.stripe.com/register)o[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fsave-and-reuse)

[

](/)

Cerca nella documentazione

/

[Crea un account](https://dashboard.stripe.com/register)

[

Accedi



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fsave-and-reuse)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

[

Strumenti di sviluppo



](/development)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Inizia



](/get-started)

[

Pagamenti



](/payments)

[

Automazione finanziaria



](/finance-automation)

[

Per piattaforme e marketplace



](/connect)

[

Banking-as-a-Service



](/financial-services)

API e SDK

Guida

[Panoramica](/payments)

Informazioni sui pagamenti con Stripe

[Eseguire l'upgrade dell'integrazione](/payments/upgrades "Migliorare l'integrazione esistente")

Analisi dei dati sui pagamenti

Pagamenti online

[Panoramica](/payments/online-payments "Opzioni di integrazione per accettare pagamenti online")[Trovare il caso d'uso più adatto](/payments/use-cases/get-started "Come Stripe può supportare l'attività")

Use Payment Links

Creare una pagina di pagamento

[Panoramica](/payments/checkout/build-integration "Crea un'esperienza di pagamento con Checkout.")

[Guide rapide](/payments/checkout/quickstarts "Iniziare con codice di esempio")

[Personalizzare l'aspetto](/payments/checkout/customization "Controlla l'aspetto della pagina di pagamento. Il livello di personalizzazione dipende dal prodotto utilizzato.")

[Raccogliere informazioni aggiuntive](/payments/checkout/collect-additional-info "Raccogli informazioni come indirizzi di spedizione e numeri di telefono nel corso della procedura di pagamento.")

[Riscuotere le imposte](/payments/checkout/taxes)

[Aggiornare la procedura di pagamento in modo dinamico](/payments/checkout/dynamic-updates "Apportare aggiornamenti mentre il cliente esegue la procedura di pagamento")

[Gestire il catalogo dei prodotti](/payments/checkout/product-catalog)

[Abbonamenti](/payments/subscriptions "Gestire gli abbonamenti con Checkout")

[Gestire i metodi di pagamento](/payments/checkout/payment-methods)

[Consentire ai clienti di pagare nella loro valuta locale](/payments/checkout/adaptive-pricing)

[Aggiungere sconti, upsell e cross-sell](/payments/checkout/promotions)

Configura pagamenti futuri

[Salvare i dati di pagamento durante il pagamento](/payments/checkout/save-during-payment "Salvare i dati di pagamento durante il pagamento")

[Dopo il pagamento](/payments/checkout/after-the-payment)

[Elements con log delle modifiche per l'API Checkout Sessions](/checkout/elements-with-checkout-sessions-api/changelog)

[Migrare da una procedura di pagamento esistente](/payments/checkout/migration)

[Migrare Checkout per utilizzare Prices](/payments/checkout/migrating-prices)

Creare un'integrazione iniziale

Creare un'integrazione in-app

Modalità di pagamento

Aggiungere modalità di pagamento

Gestire i metodi di pagamento

Pagare più velocemente con Link

Interfacce utente di pagamento

Payment Links

Checkout

Elements per il Web

Elements in-app

Scenari di pagamento

Flussi di pagamento personalizzati

Acquisizione flessibile

Pagamenti di persona

Terminal

Altri prodotti Stripe

Financial Connections

Criptovaluta

Climate

Link per bonifico

Italia

Italiano

[Pagina iniziale](/ "Pagina iniziale")[Pagamenti](/payments "Pagamenti")Build a checkout page

Set up future payments
======================

Learn how to save payment details and charge your customers later.
------------------------------------------------------------------

#### Attenzione

[SCA regulation](/strong-customer-authentication) requires that you authenticate your customer up front if you intend to collect payments from them again in the future. If the customer never authenticated initially, their bank may decline future payments and ask for additional authentication.

Stripe-hosted page

Embedded form

Embedded components

Public preview

To collect customer payment details that you can reuse later, use Checkout’s setup mode. Setup mode uses the [Setup Intents API](/api/setup_intents) to create [Payment Methods](/api/payment_methods).

Check out our [full, working sample on GitHub](https://github.com/stripe-samples/checkout-remember-me-with-twilio-verify).

[

Set up Stripe

Server-side




------------------------------





](#set-up-stripe)

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries to access the Stripe API from your application:

Command Line

Ruby

`# Available as a gem sudo gem install stripe`

Gemfile

Ruby

`# If you use bundler, you can add this line to your Gemfile gem 'stripe'`

[

Create a Checkout Session

Client-side

Server-side




-------------------------------------------------------





](#create-checkout-session)

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

index.html

`<html>   <head>     <title>Checkout</title>   </head>   <body>     <form action="/create-checkout-session" method="POST">       <button type="submit">Checkout</button>     </form>   </body> </html>`

To create a setup mode Session, use the `mode` parameter with a value of `setup` when creating the Session. You can optionally specify the [customer parameter](/api/checkout/sessions/create#create_checkout_session-customer) to automatically attach the created payment method to an existing customer. Checkout uses [Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods) by default, which requires you to pass the [currency](/api/checkout/sessions/create#create_checkout_session-currency) parameter when using `setup` mode.

Append the `{CHECKOUT_SESSION_ID}` template variable to the `success_url` to get access to the Session ID after your customer successfully completes a Checkout Session. After creating the Checkout Session, redirect your customer to the [URL](/api/checkout/sessions/object#checkout_session_object-url) returned in the response.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d mode=setup \  -d currency=usd \  -d customer=  {{CUSTOMER_ID}}   \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})"`

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn individual payment methods on or off in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). By default, Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe filters them out even when they’re enabled. We filter Google Pay if you [enable automatic tax](/tax/checkout) without collecting a shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

[

Retrieve the Checkout Session

Server-side




----------------------------------------------





](#retrieve-checkout-session)

After a customer successfully completes their Checkout Session, you need to retrieve the Session object. There are two ways to do this:

*   **Asynchronously**: Handle `checkout.session.completed` [webhooks](/webhooks "webhook"), which contain a Session object. Learn more about [setting up webhooks](/webhooks).
*   **Synchronously**: Obtain the Session ID from the `success_url` when a user redirects back to your site. Use the Session ID to [retrieve](/api/checkout/sessions/retrieve) the Session object.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions/cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :"`

The right choice depends on your tolerance for dropoff, as customers may not always reach the `success_url` after a successful payment. It’s possible for them close their browser tab before the redirect occurs. Handling webhooks prevents your integration from being susceptible to this form of dropoff.

After you have retrieved the Session object, get the value of the `setup_intent` key, which is the ID for the SetupIntent created during the Checkout Session. A [SetupIntent](/payments/setup-intents) is an object used to set up the customer’s bank account information for future payments.

Example `checkout.session.completed` payload:

`{   "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",   "object": "event",   "api_version": "2019-03-14",   "created": 1561420781,   "data": {     "object": {       "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",       "object": "checkout.session",       "billing_address_collection": null,       "client_reference_id": null,       "customer": "",       "customer_email": null,       "display_items": [],       "mode": "setup",       "setup_intent": "seti_1EzVO3HssDVaQm2PJjXHmLlM",       "submit_type": null,       "subscription": null,       "success_url": "[https://example.com/success](https://example.com/success)"     }   },   "livemode": false,   "pending_webhooks": 1,   "request": {     "id": null,     "idempotency_key": null   },   "type": "checkout.session.completed" }`

Note the `setup_intent` ID for the next step.

[

Retrieve the SetupIntent

Server-side




-----------------------------------------





](#retrieve-setup-intent)

Using the `setup_intent` ID, [retrieve](/api/setup_intents/retrieve) the SetupIntent object. The returned object contains a `payment_method` ID that you can attach to a customer in the next step.

Command Line

cURL

`curl https://api.stripe.com/v1/setup_intents/seti_1EzVO3HssDVaQm2PJjXHmLlM \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :"`

#### Nota

If you’re requesting this information synchronously from the Stripe API (as opposed to handling webhooks), you can combine the previous step with this step by [expanding](/api/expanding_objects) the SetupIntent object in the request to the /v1/checkout/session endpoint. Doing this prevents you from having to make two network requests to access the newly created PaymentMethod ID.

[

Charge the payment method later

Server-side




------------------------------------------------





](#charge-saved-payment-method)

If you didn’t create the Checkout Session with an existing customer, use the ID of the PaymentMethod to [attach](/api/payment_methods/attach) the [PaymentMethod](/api/payment_methods "PaymentMethods") to a [Customer](/api/customers "Clienti"). After you attach the PaymentMethod to a customer, you can make an off-session payment using a [PaymentIntent](/api/payment_intents/create#create_payment_intent-payment_method):

*   Set [customer](/api#create_payment_intent-customer) to the ID of the Customer and [payment\_method](/api#create_payment_intent-payment_method) to the ID of the PaymentMethod.
*   Set [off\_session](/api/payment_intents/confirm#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during a payment attempt and can’t fulfill an authentication request made by a partner, such as a card issuer, bank, or other payment institution. If, during your checkout flow, a partner requests authentication, Stripe requests exemptions using customer information from a previous on-session transaction. If the conditions for exemption aren’t met, the PaymentIntent might throw an error.
*   Set the value of the PaymentIntent’s [confirm](/api/payment_intents/create#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when you create the PaymentIntent.

Command Line

cURL

`curl https://api.stripe.com/v1/payment_intents \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d amount=1099 \  -d currency=usd \  -d customer=  {{CUSTOMER_ID}}   \  -d payment_method=  {{PAYMENT_METHOD_ID}}   \  -d off_session=true \  -d confirm=true`

When a payment attempt fails, the request also fails with a 402 HTTP status code and the status of the PaymentIntent is [requires\_payment\_method](/upgrades#2019-02-11 "requires_payment_method"). Notify your customer to return to your application (for example, by sending an email or in-app notification) and direct your customer to a new Checkout Session to select another payment method.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_9W1R4v0cz6AtC9PVwHFzywti  :" \  -d customer=  {{CUSTOMER_ID}}   \  -d "line_items[0][price_data][currency]"=usd \  -d "line_items[0][price_data][product_data][name]"=T-shirt \  -d "line_items[0][price_data][unit_amount]"=1099 \  -d "line_items[0][quantity]"=1 \  -d mode=payment \   --data-urlencode success_url="[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})"`

Questa pagina è stata utile?

SìNo

Hai bisogno di aiuto? [Contatta l'assistenza clienti](https://support.stripe.com/).

Partecipa al nostro [programma di accesso anticipato](https://insiders.stripe.dev/).

Consulta il nostro [registro delle modifiche al prodotto](https://stripe.com/blog/changelog).

Domande? [Contattaci](https://stripe.com/contact/sales).

Realizzato da [Markdoc](https://markdoc.dev)

Registrati per ricevere gli aggiornamenti destinati agli sviluppatori:

Registrati

Puoi annullare l'iscrizione in qualsiasi momento. Leggi la nostra [informativa sulla privacy](https://stripe.com/privacy).

In questa pagina

[Set up Stripe](#set-up-stripe "Set up Stripe")

[Create a Checkout Session](#create-checkout-session "Create a Checkout Session")

[Payment methods](#payment-methods "Payment methods")

[Retrieve the Checkout Session](#retrieve-checkout-session "Retrieve the Checkout Session")

[Retrieve the SetupIntent](#retrieve-setup-intent "Retrieve the SetupIntent")

[Charge the payment method later](#charge-saved-payment-method "Charge the payment method later")

Prodotti utilizzati

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

La shell di Stripe offre prestazioni ottimali in versione desktop.

    $

---

## URL: https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=embedded-form&oo-step=true&should-crawl=true&record-id=2b2gg6z00u&wait-before-scraping=2000&save-html=true&save-markdown=true

 How Checkout works | Stripe Documentation     

[Skip to content](#main-content)

How Checkout works

[

Create account



](https://dashboard.stripe.com/register)or[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

](/)

Search the docs or ask a question

/

[Create account](https://dashboard.stripe.com/register)

[

Sign in



](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

[

Developer tools



](/development)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Get started



](/get-started)

[

Payments



](/payments)

[

Finance automation



](/finance-automation)

[

Platforms and marketplaces



](/connect)

[

Banking as a service



](/financial-services)

APIs & SDKs

Help

[Overview](/payments)

About Stripe payments

[Upgrade your integration](/payments/upgrades "Improve your existing integration")

Payments analytics

Online payments

[Overview](/payments/online-payments "Learn about integration choices for accepting payments online.")[Find your use case](/payments/use-cases/get-started "Learn how Stripe can support your business.")

Use Payment Links

Build a checkout page

Build an advanced integration

Build an in-app integration

Payment methods

Add payment methods

Manage payment methods

Faster checkout with Link

Payment UIs

Payment Links

Checkout

[Overview](/payments/checkout)

How Checkout works

Web Elements

In-app Elements

Payment scenarios

Custom payment flows

Flexible acquiring

In-person payments

Terminal

Other Stripe products

Financial Connections

Crypto

Climate

Payout Links

Netherlands

English (United States)

[Home](/ "Home")[Payments](/payments "Payments")Checkout

How Checkout works
==================

Learn how to use Checkout to collect payments on your website.
--------------------------------------------------------------

Checkout is a low-code payment integration that creates a customizable form for collecting payments.

Checkout’s built-in features allow you to reduce your development time. It supports 40+ payment methods, including [Link](/payments/link), which lets your customers save their payment method for faster checkout. You can accept payments by embedding Checkout directly into your website, redirecting customers to a Stripe-hosted payment page, or creating a customized checkout page with [Stripe Elements](/payments/elements). Checkout supports payments for both [one-time purchases](/payments/online-payments) and [subscriptions](/subscriptions).

You can also customize Checkout and access additional functionality with the [Checkout Sessions API](/api/checkout/sessions) and the Stripe Dashboard. For a complete list of features, see its [built-in and customizable features](/payments/checkout/how-checkout-works#features).

Stripe-hosted page

Embedded form

Embedded components

Public preview

Checkout lifecycle
------------------

1.  When a customer is ready to complete their purchase, your application creates a new Checkout Session.
2.  You mount Checkout as an embeddable component on your website to show a payment form.
3.  Customers enter their payment details and complete the transaction.
4.  After the transaction, the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) webhook event triggers the [order fulfillment process](/checkout/fulfillment).

Client

Server

Stripe API

Stripe Checkout

Send order information

Create Checkout Session

Return Checkout Session

checkout.session.created

Return Checkout Session client secret

Mount Checkout on your website

Customer completes payment

Customer returns to your website

Handle fulfillment

checkout.session.completed

A diagram of an embedded form integration's lifecycle

Low-code integration
--------------------

Checkout requires minimal coding and is the best choice for most integrations because of its prebuilt functionalities and customization options. You can integrate Checkout by creating a Checkout Session and collecting customer payment details. Collect payment by [embedding a payment form](/payments/accept-a-payment?platform=web&ui=embedded-form) in your website.

[Compare Checkout](/payments/online-payments#compare-features-and-availability) to other Stripe payment options to determine the best one for you. Checkout displays a payment form to collect customer payment information, validates cards, handles errors, and so on.

Built-in and customizable features
----------------------------------

Stripe Checkout has the following built-in and customizable features:

### Built-in features

*   Support for digital wallets and Link
*   Responsive mobile design
*   SCA-ready
*   CAPTCHAs
*   PCI compliance
*   Card validation
*   Error messaging
*   [Adjustable quantities](/payments/checkout/adjustable-quantity)
*   [Automatic tax collection](/tax/checkout)
*   International language support
*   [Adaptive Pricing](/payments/checkout/adaptive-pricing)

### Customizable features

*   [Collect taxes](/payments/checkout/taxes)
*   [Custom branding with colors, buttons, and font](/payments/checkout/customization)
*   [Cross-sells](/payments/checkout/cross-sells)
*   [Global payment methods](/payments/dashboard-payment-methods)
*   [Subscription upsells](/payments/checkout/upsells)
*   [Custom domains](/payments/checkout/custom-domains) (Stripe-hosted page only)
*   [Email receipts](/receipts)
*   [Apply discounts](/payments/checkout/discounts)
*   [Custom success page](/payments/checkout/custom-success-page)
*   [Recover abandoned carts](/payments/checkout/abandoned-carts)
*   [Autofill payment details with Link](/payments/checkout/customization/behavior#link)
*   [Collect Tax IDs](/tax/checkout/tax-ids)
*   [Collect shipping information](/payments/collect-addresses?payment-ui=checkout)
*   [Collect phone numbers](/payments/checkout/phone-numbers)
*   [Set the subscription billing cycle date](/payments/checkout/billing-cycle)

### Custom branding

You can set fonts, colors, icons, and field styles for your embedded form using the [Branding settings](https://dashboard.stripe.com/settings/branding/checkout) in the Dashboard. For more information, see [Customize your integration](/payments/checkout/customization).

Checkout Session
----------------

The Checkout Session is a programmatic representation of what your customers see on the payment form. After creating a Checkout Session, mount Checkout on your payment page to complete the purchase. When customers complete their purchase, you can [fulfill their orders](/checkout/fulfillment) by configuring an [event destination](/event-destinations) to process Checkout Session events. This code snippet from the [quickstart guide](/checkout/quickstart) is an example of how to create a Checkout Session in your application.

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d "line_items[0][price]"=  {{PRICE_ID}}   \  -d "line_items[0][quantity]"=1 \  -d mode=payment \  -d ui_mode=embedded \   --data-urlencode return_url="[https://example.com/return](https://example.com/return)"`

### One-time and recurring payments

Allow customers to make one-time payments or subscribe to a product or service by setting the [mode](/api/checkout/sessions/create#create_checkout_session-mode) parameter in a Checkout Session.

Mode

Purchase type

Payment

One-time purchases

[Subscription](/billing/subscriptions/overview)

*   Recurring purchases
*   Mixed cart: Recurring purchases with one-time purchases

### Mixed cart

Create a mixed cart in Checkout that lets your customers purchase Subscription items and one-time purchase items at the same time. To create a mixed cart, set the `mode` parameter to `subscription` and include the Price IDs, or `price_data`, for each line\_item in the [line\_items](/api/checkout/sessions/create#create_checkout_session-line_items) array. Price IDs come from Price objects created using the Stripe Dashboard or API and allow you to store information about your product catalog in Stripe.

You can also use [price\_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data) to reference information from an external database where you’re hosting price and product details without storing product catalog information on Stripe. For more information, see [Build a subscriptions integration](/billing/subscriptions/build-subscriptions).

Command Line

cURL

`curl https://api.stripe.com/v1/checkout/sessions \  -u "  sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz  :" \  -d "line_items[0][price]"={{RECURRING_PRICE_ID}} \   -d "line_items[0][quantity]"=1 \  -d "line_items[1][price]"={{ONE_TIME_PRICE_ID}} \   -d "line_items[1][quantity]"=1 \  -d mode=subscription \  -d ui_mode=embedded \   --data-urlencode return_url="https://example.com/return"`

### Payment methods

You can view, enable, and disable different payment methods in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) at any time. Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. View our [complete list of payment methods](/payments/payment-methods/overview).

### Save payment details and default payment methods

You can [save payment details for future use](/payments/save-and-reuse) by sending an API parameter when you create a Session. Options to save payment details include:

*   **Single payment**: If your Checkout Session uses `payment` mode, set the [payment\_intent\_data.setup\_future\_usage](/payments/payment-intents#future-usage) parameter.
*   **Subscription payment**: If your Checkout Session uses `subscription` mode, Stripe saves the payment method by default.
*   [Multiple saved payment methods](/payments/accept-a-payment?platform=web&ui=checkout#save-payment-method-details): If a customer has multiple payment methods saved, you can store a default payment method to the Customer object’s [default\_payment\_method](/api/customers/object#customer_object-invoice_settings-default_payment_method) field. However, these payment methods don’t appear for return purchases in Checkout.

### Guest customers

The `Customer` object represents a customer of your business, and it helps tracking subscriptions and payments that belong to the same customer. Checkout Sessions that don’t create Customers are associated with [guest customers](/payments/checkout/guest-customers) instead.

Complete a transaction
----------------------

To automate business flows after a transaction has occurred, register an [event destination](/event-destinations) and build a [webhook endpoint handler](/webhooks/quickstart). Consider the following events and automations to enable:

*   Process the [checkout.session.completed](/api/events/types#event_types-checkout.session.completed) event to fullfill orders when a customer completes their purchase
*   Process the [checkout.session.expired](/api/events/types#event_types-checkout.session.expired) event to return items to your inventory or send users a cart [abandonment](/payments/checkout/abandoned-carts) email when they don’t make a purchase and their cart expires

See also
--------

*   [Checkout quickstart](/checkout/quickstart)
*   [Fulfill your orders](/checkout/fulfillment)
*   [Collect taxes in Checkout](/payments/checkout/taxes)
*   [Manage limited inventory with Checkout](/payments/checkout/managing-limited-inventory)
*   [Automatically convert to local currencies with Adaptive Pricing](/payments/checkout/adaptive-pricing)

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [product changelog](https://stripe.com/blog/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev)

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Checkout lifecycle](#lifecycle "Checkout lifecycle")

[Low-code integration](#low-code "Low-code integration")

[Built-in and customizable features](#features "Built-in and customizable features")

[Built-in features](#built-in "Built-in features")

[Customizable features](#customizable "Customizable features")

[Custom branding](#branding "Custom branding")

[Checkout Session](#session "Checkout Session")

[One-time and recurring payments](#checkout-mode "One-time and recurring payments")

[Mixed cart](#mixed-cart "Mixed cart")

[Payment methods](#payment-methods "Payment methods")

[Save payment details and default payment methods](#save-payment-methods "Save payment details and default payment methods")

[Guest customers](#guest-customers "Guest customers")

[Complete a transaction](#complete-transaction "Complete a transaction")

[See also](#see-also "See also")

Related Guides

[

No-code options to accept payments on Stripe



](/no-code)

[

Prebuilt checkout page



](/checkout/quickstart)

[

Learn about payment methods



](/payments/payment-methods/overview)

Products Used

[

Checkout





](/payments/checkout)

Stripe Shell

Test mode

API Explorer

[

](https://stripe.com/docs/stripe-cli#install)

    
    Welcome to the Stripe Shell!
    
    Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
    Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
    resources in test mode.
    
    - View supported Stripe commands: stripe help ▶️
    - Find webhook events: stripe trigger ▶️ [event]
    - Listen for webhook events: stripe listen ▶
    - Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)
    

The Stripe Shell is best experienced on desktop.

    $

---

