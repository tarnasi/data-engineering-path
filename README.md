# Data Engineering Learning Path

## 🏢 Company: NovaMart (E-Commerce)

**NovaMart** is a mid-sized e-commerce platform selling electronics, home goods, and fashion items across North America. The company processes ~500K orders/month, serves 2M+ active users, and is growing fast.

### Data Landscape

| Source | Description |
|---|---|
| PostgreSQL (OLTP) | Core transactional DB — orders, users, products, payments |
| MongoDB | Product catalog, reviews, recommendations |
| Application Logs | Clickstream, search queries, error logs (JSON, shipped to S3) |
| Third-Party APIs | Stripe (payments), Shippo (shipping), Google Analytics |
| Kafka | Real-time events — cart actions, inventory changes, user sessions |
| CSV/FTP Feeds | Vendor inventory files, marketing campaign data |

### Tech Stack (evolves as you progress)

- **Beginner**: SQL, Python, CSV/JSON, pandas, PostgreSQL basics
- **Junior**: SQL, Python, PostgreSQL, repeatable pipelines, intro Airflow, intro dbt
- **Mid-Level**: Spark, Snowflake/BigQuery, Airflow (advanced), dbt (advanced), data quality frameworks
- **Senior**: Kafka, Flink, system design, cost optimization, observability, architecture

---

## 📁 Curriculum Structure

Each level now has its own folder with a consistent study layout:

- `roadmap.md`: what to learn, how long it should take, and when to move on
- `how_to_work.md`: how to do homework and what you must explain after each task
- `checkpoint_test.md`: mid-level check before continuing
- `final_test.md`: end-of-level mastery test

| Level | Folder | Task Source |
|---|---|---|
| Beginner | `beginner/` | Uses Junior Tasks 1–5 as foundation work |
| Junior | `junior/` | `junior/tasks_001_020.md` through `junior/tasks_081_100.md` |
| Mid | `mid/` | `mid/tasks_101_120.md` through `mid/tasks_196_200.md` |
| Senior | `senior/` | `senior/tasks_201_205.md` through `senior/tasks_256_260.md` |

---

## 🚀 How to Use

1. Start in `beginner/` and follow the level roadmap before jumping to higher folders.
2. Work through tasks sequentially inside the mapped level.
3. After each task, use the level's `how_to_work.md` file to explain what you built and why.
4. Take the `checkpoint_test.md` before moving into the second half of a level.
5. Take the `final_test.md` before moving to the next level.
6. If you fall behind, extend the schedule instead of compressing the learning.

---

## 📊 Core Database Schema (NovaMart PostgreSQL)

```sql
-- users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    country VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE
);

-- products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    subcategory VARCHAR(100),
    price NUMERIC(10,2),
    cost NUMERIC(10,2),
    vendor_id INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    is_active BOOLEAN DEFAULT TRUE
);

-- orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    order_date TIMESTAMP DEFAULT NOW(),
    status VARCHAR(50), -- 'pending','confirmed','shipped','delivered','cancelled','returned'
    total_amount NUMERIC(10,2),
    shipping_address_id INTEGER,
    payment_method VARCHAR(50),
    coupon_code VARCHAR(50)
);

-- order_items
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER,
    unit_price NUMERIC(10,2),
    discount NUMERIC(10,2) DEFAULT 0
);

-- payments
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    payment_date TIMESTAMP,
    amount NUMERIC(10,2),
    method VARCHAR(50), -- 'credit_card','debit_card','paypal','apple_pay'
    status VARCHAR(50), -- 'success','failed','refunded'
    stripe_charge_id VARCHAR(100)
);

-- vendors
CREATE TABLE vendors (
    vendor_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_email VARCHAR(255),
    country VARCHAR(50),
    rating NUMERIC(3,2)
);

-- product_reviews
CREATE TABLE product_reviews (
    review_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    user_id INTEGER REFERENCES users(user_id),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- shipping
CREATE TABLE shipping (
    shipping_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    carrier VARCHAR(50),
    tracking_number VARCHAR(100),
    shipped_date TIMESTAMP,
    delivered_date TIMESTAMP,
    status VARCHAR(50) -- 'processing','in_transit','delivered','failed'
);

-- clickstream_events (loaded from logs)
CREATE TABLE clickstream_events (
    event_id BIGSERIAL PRIMARY KEY,
    user_id INTEGER,
    session_id VARCHAR(100),
    event_type VARCHAR(50), -- 'page_view','add_to_cart','search','checkout_start','purchase'
    page_url TEXT,
    referrer_url TEXT,
    event_timestamp TIMESTAMP,
    device_type VARCHAR(20),
    browser VARCHAR(50)
);
```

---

## 🗂 Sample Data Sources

| Dataset | Link / Format |
|---|---|
| Brazilian E-Commerce (Olist) | [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| Online Retail II | [Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) |
| Instacart Market Basket | [Kaggle](https://www.kaggle.com/datasets/yasserh/instacart-online-grocery-basket-analysis-dataset) |
| E-Commerce Events (REES46) | [Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop) |
| Clickstream Data | [Kaggle](https://www.kaggle.com/datasets/tunguz/clickstream-data-for-online-shopping) |

Use these as substitutes or supplements. Adapt column names to match NovaMart's schema.
