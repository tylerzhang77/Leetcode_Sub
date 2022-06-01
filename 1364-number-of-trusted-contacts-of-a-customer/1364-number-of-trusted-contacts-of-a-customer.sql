# Write your MySQL query statement below
SELECT i.invoice_id,
       c.customer_name,
       i.price,
       COUNT(distinct t.contact_name) as contacts_cnt,
       SUM(CASE WHEN contact_name
            IN (select distinct customer_name from Customers)
            THEN 1 ELSE 0 END) as trusted_contacts_cnt
FROM Invoices as i
JOIN Customers as c on c.customer_id = i.user_id
LEFT JOIN Contacts as t on c.customer_id = t.user_id
GROUP BY i.invoice_id