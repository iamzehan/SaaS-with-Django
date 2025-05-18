#django #SaaS #postgreSQL #neon_postgres 

---
- This course is designed to be a **foundation** for building a **SaaS application**.
- The goal is to provide something that can be **built off of** to create a **functioning SaaS application** where you can **start charging users**, build out **customers**, and **launch a startup**.
- It includes foundations with **billing already in place** and **user permissions already in place**.
- There is an invitation for suggestions on what should be built on top of this foundation in the future.
- Possible future directions mentioned include improving the frontend with technologies like **Next**, **React**, or **HTMX**.

# **Free Code Available**

- The **code for the SaaS Foundations course is available** [here](https://github.com/iamzehan/SaaS-Foundations)
- It is described as **foundational code** that you can **iterate and build on top of** for **any of your projects at any time**.
- The code is located on **GitHub**.
- Specifically, it's in the SAS foundation's **actual code repository**.
- The repository can be found at **cf. GitHub**.
- You can **Fork it and give it a run**.
- It is recommended to go through the **README file to get it working correctly**.
- A lot of code is covered to ensure your application is **up and running** and you have these foundations down.

# **Django Framework Fundamentals**

- The project uses **Django**.
- **Django apps** are smaller components that build up the entire project.
- There are **built-in applications** that come with Django by default, such as users, user sessions, and the Django admin.
- **settings.py** is where various components and configurations of the Django project are managed.
- **INSTALLED_APPS** in `settings.py` lists all the components that make up the project.
- The Django **ORM (Object-Relational Mapper)** is used to save and retrieve data, primarily through **models**.
- The **Django admin** provides an entry point to manage data and users within the Django project. It's described as one of Django's more powerful features.
- Aspects of the Django admin are emulated in the project.
- Django has built-in ways to handle **data validation**.

# **Templating and Styling**

- **Django templates** are used for rendering HTML.
- **Context processors** can build out variables available to every template.
- The structure involves a **base.html** template.
- External files for **CSS** and **JavaScript** are included in the base template, often in separate HTML files (e.g., `base/css.html`, `base/javascript.html`) and included using template tags.
- Keeping templates narrow and specific makes projects easier to manage as complexity grows and helps in seeing changes inside **git** (version control).
- [**Flowbite**](https://flowbite.com/docs/getting-started/django/) is mentioned and used for styling components like the nav bar and pricing tables, leveraging [**TailwindCSS**](https://tailwindcss.com/) utility classes.
- Snippets (e.g., `pricing_card.html`) are used to break down larger templates into reusable components.

# **Authentication and Users**

- Django comes with a **built-in user system** for logins, groups, and sessions.
- Creating a **super user** is necessary to log into the Django admin initially.
- The course implements **user registration**.
- **Login** and **logout** functionality is implemented.
- The **Django-allauth** package is integrated for authentication, offering features like email-based login and social account providers.
- Django-allauth configuration includes settings for **authentication methods** (e.g., username, email, username/email) and **email required**.
- Email verification can be made **mandatory** using Django-allauth settings.
- Redirects after login can be configured in Django settings.
- Social account providers like **GitHub** can be integrated through Django-allauth.
- Templates for Django-allauth (like login, logout, signup) need to be modified to fit the project's branding and design.

# **Permissions and Authorization**

- The course covers **permissions and authorization** – defining what users are allowed to do.
- Simple **password-protected pages** can be implemented.
- **Django's built-in admin permissions** can be used to manage user capabilities within the admin interface.
- Granting too many permissions in the admin can lead to unintended consequences.
- It's often recommended in SaaS applications to **customize your own permissions** rather than solely relying on the default Django admin permissions.
- Users have a `has_perm` method to check if they have a specific permission.
- Permissions are updated as you add more models.
- You can list available permissions using the Django admin shell and the `Permission` model.
- Permissions can be chained together in logic.
- **Groups** can be created in the Django admin to bundle permissions.
- Users can be added to groups, inheriting the group's permissions.
- Groups can represent different **subscription levels** (e.g., Basic Plan, Pro Plan).
- Accessing user groups directly (`user.groups.all()`) is possible but filtering based on group names in code is **not ideal** because changing the group name requires code changes.
- It's better to use **permissions** to control access based on subscription levels.
- **Custom permissions** can be defined within a model's `Meta` class. These permissions can be specific to subscription plans.
- A **Subscription model** is created to track subscription plans and define custom permissions (e.g., 'basic', 'pro', 'advanced').
- Group permissions need to be **synced** with the custom permissions defined in the Subscription model.
- A custom **Django management command** (`sync_user_subs`) is created to ensure group permissions match the subscription permissions, acting as a "healing" mechanism. This sync can happen over time or on demand.
- The Subscription model is set up to be in charge of ensuring those permissions work correctly.
- Managing user memberships in groups can involve checking current groups, desired groups (from subscriptions), and adding/removing users from groups based on set operations (union, difference).

# **Billing and Subscriptions (Stripe)**

- The application integrates with **Stripe** for handling **reoccurring transactions** (subscriptions).
- A dedicated **billing.py** module is created in a `helpers` folder to centralize Stripe API keys and calls. This makes it easier to manage API changes and potentially switch payment processors later.
- Stripe **API keys** are obtained from the Stripe Dashboard Developers section.
- **Environment variables** (`.env`) and **Decouple** are used to securely store API keys and other sensitive settings. Test secret keys start with `sk_test`.
- The course implements the process of **creating customers in Stripe** via the API.
- A local **Django customer model** is created to link Django users to their corresponding Stripe customer ID. This ID is crucial for referencing the customer in Stripe.
- The Stripe customer ID starts with `cus_`.
- **Metadata** (e.g., user ID, username) can be passed when creating a Stripe customer to link it back to the Django user in the Stripe dashboard. The more metadata, the easier it is to manage.
- The difference between **production and development** Stripe environments is highlighted – customers created in one won't exist in the other.
- **Products** are created in Stripe, representing the subscription plans.
- A **Subscription model** is used to correspond to Stripe products.
- When creating a Stripe product, metadata like the local subscription plan ID can be included.
- **Prices** are created in Stripe and linked to products.
- A separate **Subscription Price model** is created to link local pricing details to Stripe prices. This model has a ForeignKey relationship to the Subscription model.
- Prices can be for **monthly** or **yearly** intervals.
- A `TextChoices` class is used to define the available price intervals (month, year).
- Prices include a **currency** (e.g., USD) and a **unit amount**.
- The unit amount is stored as an integer in Stripe and needs to be converted from decimal values (e.g., multiplying by 100 for USD).
- Stripe price IDs start with `price_`.
- Subscription price objects are set up so they **cannot be deleted** in the Django admin (`can_delete = False`).
- An **active** field will be needed on the Subscription Price model to manage which prices are currently in use.
- The **pricing page** displays the different subscription plans and their prices.
- Pricing plans can have **features** or **benefits**, stored as text (separated by newlines) on the Subscription model and processed into a list for display.
- The pricing page can include **tabs** to toggle between monthly and yearly pricing intervals, typically handled by passing the interval as a parameter in the URL and filtering the query set in the view.
- A **checkout process** is initiated by clicking a "Get Started" button on a pricing plan, which redirects the user.
- The selected price ID is stored in the user's session during the checkout process.
- A local **User Subscription model** is likely used (though not explicitly created in name, the process describes a model tracking user subscriptions based on Stripe data) to store the link between a user and their active subscription, including details like Stripe subscription ID, price ID, and cancellation status.
- The checkout success view processes the Stripe checkout session data and updates the local user subscription model, including handling cancellation status.
- Query sets are used to filter active or trialing subscriptions for users.

# **Database Management**

- Data is stored using **Django's models**, which map to database tables.
- Each field in a model maps to a column in the database table.
- An invisible **ID** column is the **primary key** and is an auto-incrementing integer by default.
- Various **model field types** are available (e.g., `TextField`, `DateTimeField`, `CharField`, `ForeignKey`, `ManyToManyField`) and are crucial for database effectiveness and optimization.
- The **Django documentation** is the place to find information on available model fields.
- **Query sets** are used to retrieve data from the database based on models.
- The **Q lookup** (`from django.db.models import Q`) allows chaining multiple lookup conditions in filters using logical operators like `|` (OR).
- **ForeignKey** defines a many-to-one relationship. `on_delete=models.SET_NULL` means the foreign key is set to null if the referenced object is deleted.
- **ManyToManyField** defines a many-to-many relationship, used implicitly with Users and Groups. Managing these relationships can involve working with sets of IDs.
- **Neon PostgreSQL** is mentioned as the database, particularly in the context of database branching for testing and automation.

# **Deployment and Automation (GitHub Actions, Neon)**

- **GitHub Actions** are used for **CI/CD (Continuous Integration and Continuous Delivery/Deployment)**.
- GitHub Actions can also be used for **serverless scheduling**.
- **Neon's database branching** feature is utilized with GitHub Actions. This allows creating branched versions of the database for testing or analysis without affecting the production database.
- The **Neon CLI** (Command Line Interface) is used within GitHub Actions workflows to automate database branching.
- Workflows are defined in YAML files located in `.github/workflows/`.
- Workflows involve steps like setting up Python, checking out code, setting up Node.js (for Neon CLI), installing dependencies, and running commands.
- **Scheduled jobs** can be set up in GitHub Actions using cron syntax.
- Custom **Django management commands** (like `sync_user_subs` and `clear_dangling`) are run on a schedule using GitHub Actions.
- Conditional logic (`if:`) in workflow steps can be used to skip steps based on the event that triggered the workflow (e.g., skipping a command unless triggered by a specific schedule).

# **Project Structure and Practices**

- The project is organized using standard Django practices: separating components into **apps**, managing settings in `settings.py`, defining data structures in `models.py`, handling logic in `views.py`, and routing requests in `urls.py`.
- Templates are organized with a `base.html` and includes/snippets for reusable parts.
- Using environment variables and **Decouple** is emphasized for managing settings and secrets.
- Centralizing third-party API calls (like Stripe) in a dedicated **helpers** module improves organization and maintainability.
- Using version control like **Git** is mentioned for tracking changes.
- Defining choices for model fields using `models.TextChoices` is demonstrated for clarity and consistency.
- Using the **Django admin** for testing and managing data is frequently shown.
- Serialization is used to structure data retrieved from external APIs (like Stripe) before updating local models.
- Using `try...except` blocks is shown for handling potential errors gracefully.
- Working with **sets** is used for efficiently managing relationships like user groups.