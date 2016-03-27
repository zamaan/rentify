import requests

def send_request_email(owner_email,r_item):
        return requests.post(
        "https://api.mailgun.net/v3/sandbox9a70a48d57e64a8ba860ebe39c34b025.mailgun.org/messages",
        auth=("api", "key-a8640ae445de55dfb1f2aaba351581dd"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox9a70a48d57e64a8ba860ebe39c34b025.mailgun.org>",
              "to": "%s"%owner_email,
              "subject": "Rental Request from RentXYZ.in",
              "text": "Hey! You have got a request from %s for item : %s. Duration is %s weeks. Visit rentxyz.in/requests to approve or deny"%(r_item.user.profile_set.get().full_name,r_item.item.name,r_item.duration)})

def send_approve_email(renter_email,r_item):
        return requests.post(
        "https://api.mailgun.net/v3/sandbox9a70a48d57e64a8ba860ebe39c34b025.mailgun.org/messages",
        auth=("api", "key-a8640ae445de55dfb1f2aaba351581dd"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox9a70a48d57e64a8ba860ebe39c34b025.mailgun.org>",
              "to": "%s"%renter_email,
              "subject": "Rental Request Approved! - RentXYZ.in",
              "text": "Hey! Your request for %s has been approved. Here is the phone number : %s and address of the owner %s. Get in touch to arrange the exchange. Hope you liked our service."%(r_item.item.name,r_item.item.user.profile_set.get().phone_number,r_item.item.user.profile_set.get().address)})

def send_deny_email(renter_email,r_item):
        return requests.post(
        "https://api.mailgun.net/v3/sandbox9a70a48d57e64a8ba860ebe39c34b025.mailgun.org/messages",
        auth=("api", "key-a8640ae445de55dfb1f2aaba351581dd"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox9a70a48d57e64a8ba860ebe39c34b025.mailgun.org>",
              "to": "%s"%renter_email,
              "subject": "Rental Request Denied! - RentXYZ.in",
              "text": "Hey! Your request for %s has been denied by the item owner. Explore other items here rentxyz.in/items"%r_item.item.name})

def requests_for_user(user):
    requests = []
    user_items = user.item_set.all()
    for item in user_items:
        for i in item.requestitem_set.filter(status="requested"):
            requests.append(i)
    requests_count = len(requests)

    return requests, requests_count