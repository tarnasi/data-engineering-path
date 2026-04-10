-- How many prders exist
select COUNT(*) from orders;

-- What is the date range?
select
	MIN(order_purchase_timestamp::timestamp) as min_date_purchase,
	MAX(order_purchase_timestamp::timestamp) as max_date_purchase,
	MAX(order_purchase_timestamp::timestamp) - MIN(order_purchase_timestamp::timestamp) as total_range_of_purchase
from orders;

-- how many users places order
select COUNT(distinct customer_id) from orders;

-- How many orders each customer has.
select customer_id, COUNT(*) from orders group by customer_id;

-- How many have never ordered?
select COUNT(*)
from customers c
left join orders o
	on c.customer_id = o.customer_id
where o.customer_id is null;


-- What % of orders are in each status?
select
	order_status as "Status",
	COUNT(*) as "Order Count",
	ROUND(1000.0 * COUNT(*) / (select count(*) from orders), 2) as "Percentage"
from orders
group by order_status;


