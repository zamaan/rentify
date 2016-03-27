import requests
def send_request_email(owner_email,r_item):
        return requests.post(
        "https://api.mailgun.net/v3/sandbox9a70a48d57e64a8ba860ebe39c34b025.mailgun.org/messages",
        auth=("api", "key-a8640ae445de55dfb1f2aaba351581dd"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox9a70a48d57e64a8ba860ebe39c34b025.mailgun.org>",
              "to": "%s"%owner_email,
              "subject": "Rental Request from RentXYZ.in",
              "text": "Hey! You have got a request from %s for item : %s. Duration is %d weeks. Visit rentxyz.in/requests to approve or deny"%(r_item.user.profile_set.get().full_name,r_item.item.name,r_item.duration)})