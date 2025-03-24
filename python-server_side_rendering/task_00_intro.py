def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("format error")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("attendees error")
        return
    if not template:
        print("template is empty")
        return
    if not attendees:
        print("no data provided")
        return

    for n, attendee in enumerate(attendees, start=1):
        output_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output_content = output_content.replace(f"{{{key}}}", value)

        output_filename = f"output_{n}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)