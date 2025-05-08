sql_query_prompts = [
#     # Easy Level
#     "Retrieve all purchase orders (po) with their statuses.",
#     "Fetch the descriptions of all purchase orders from the po_description table.",
#     "List all items in the PurchaseOrderQuantities table with their quantities and unit prices.",
#     "Get the total number of purchase orders in the po table.",
#     "Find all purchase orders with a status of 'success'.",\
#     "Fetch the PO_ID and description for all purchase orders.",
#     "List all unique statuses in the po table.",
#     "Get the PO_ID and total price for all purchase orders in the PurchaseOrderQuantities table.",
#     "Retrieve all purchase orders with a status of 'failure'.",

#     # Medium Level
#     "Fetch all purchase orders along with their descriptions by joining the po and po_description tables.",
#     "List all purchase orders along with the total quantity of items ordered for each PO_ID.",
#     "Retrieve the PO_ID, Item_ID, and total price for all items in the PurchaseOrderQuantities table.",
#     "Find all purchase orders where the total price exceeds 1000.",
#     "Get the PO_ID and the number of items ordered for each purchase order.",
#     "Fetch all purchase orders along with their descriptions where the status is 'success'.",
#     "List all purchase orders along with the total price of items ordered for each PO_ID.",
#     "Fetch the PO_ID and description for all purchase orders where the description contains the word 'urgent'.",
#     "List all purchase orders along with the total price and total quantity of items ordered.",

#     # Advanced Level
#     "Fetch all purchase orders along with their descriptions and total prices by joining all three tables.",
#     "List all purchase orders where the total price is greater than the average total price of all purchase orders.",
#     "Retrieve the PO_ID and the total number of items ordered for each purchase order, sorted by the total quantity in descending order.",
#     "Find all purchase orders where the total price is greater than 500 and the status is 'success'.",
#     "List all purchase orders along with their descriptions and the total quantity of items ordered for each PO_ID.",
#     "Retrieve the PO_ID and the total price for all purchase orders, grouped by PO_ID and sorted by total price in descending order.",
#     "Fetch all purchase orders where the description contains the word 'priority' and the total price exceeds 1000.",
#     "List all purchase orders along with their statuses, descriptions, and total prices, grouped by PO_ID.",
#     "Retrieve the PO_ID, Item_ID, and total price for all items where the unit price is greater than 50.",

#     # Highly Complex Level
#     "Fetch all purchase orders along with their descriptions, total prices, and total quantities, grouped by PO_ID and sorted by total price in descending order.",
#     "List all purchase orders where the total price is greater than the average total price of all purchase orders and the status is 'success'.",
#     "Fetch all purchase orders along with their descriptions and total prices, where the total price exceeds 1000 and the description contains the word 'urgent'.",
#     "List all purchase orders along with their statuses, descriptions, total prices, and total quantities, grouped by PO_ID and sorted by total quantity in descending order.",
#     "Retrieve the PO_ID and the total price for all purchase orders where the total price is greater than the average total price of all purchase orders, grouped by PO_ID.",
#     "Fetch all purchase orders along with their descriptions, total prices, and total quantities, where the total price exceeds 500 and the status is 'success'.",
#     "List all purchase orders along with their statuses, descriptions, total prices, and total quantities, grouped by PO_ID and sorted by total price in descending order.",
#     "Fetch all purchase orders along with their descriptions, total prices, and total quantities, where the total price exceeds 1000 and the description contains the word 'priority'.",
#     "List all purchase orders along with their statuses, descriptions, total prices, and total quantities, grouped by PO_ID and sorted by total quantity in descending order.",
#     "Retrieve the PO_ID and the total price for all purchase orders where the total price is greater than the average total price of all purchase orders, grouped by PO_ID and sorted by total price in descending order.",
#     "Fetch all purchase orders along with their descriptions, total prices, and total quantities, where the total price exceeds 500 and the status is 'success', grouped by PO_ID.",
#     "List all purchase orders along with their statuses, descriptions, total prices, and total quantities, grouped by PO_ID and sorted by total price in descending order.",
#     "Fetch all purchase orders along with their descriptions, total prices, and total quantities, where the total price exceeds 1000 and the description contains the word 'urgent', grouped by PO_ID.",
#     "List all purchase orders along with their statuses, descriptions, total prices, and total quantities, grouped by PO_ID and sorted by total quantity in descending order.",
#     "Retrieve the PO_ID and the total price for all purchase orders where the total price is greater than the average total price of all purchase orders, grouped by PO_ID and sorted by total price in descending order.",
# #     "Fetch all purchase orders along with their descriptions, total prices, and total quantities, where the total price exceeds 500 and the status is 'success', grouped by PO_ID and sorted by total price in descending order."
#     "Fetch all purchase orders that do not have any description in the po_description table.",
#     "List the PO_IDs for which the total quantity of items ordered is zero.",
#     "Find all purchase orders where at least one item's unit price is less than 10.",
#     "List all purchase orders along with the count of distinct items ordered for each PO_ID.",
#     "Fetch the PO_ID and status for all purchase orders where the description contains the word 'delayed'."
    "List all purchase orders in. the order of the creattion date",
    "Retrieve the PO_IDs of purchase orders that have the status as failure along with description"
]
