# List to store all event details
events = []

n = int(input("Enter number of flag hoisting locations: "))
print(n)

# Check if n is less than or equal to 0
if n <= 0:
    print("\n❌ You have entered an invalid number of locations.")
    print("⚠️ It is not possible to prepare a flag hoisting report without valid data.")
    print("🔁 Please run the program again and enter at least one location.")
    print("🙏 JAI HIND 🙏")
else:
    # Run the for loop with the range of 'n' value
    for i in range(n):
        print("\n📍 Location", i + 1)
        location = input("🏫 Enter location name: ").strip()
        print("➡️", location)
        
        participants = int(input("👥 Enter number of participants: "))
        print("➡️", participants)
        
        time = input("⏰ Enter flag hoisting time (HH:MM): ")
        print("➡️", time)
        print("\n----------------------------------------------------------------")

        # Creating a dictionary
        event = {
            "location": location,
            "participants": participants,
            "time": time
        }

        # Append the event dictionary to the events list
        events.append(event)

    # Initialize total participants to 0
    total = 0

    # Set both max_event and min_event to the first event
    max_event = events[0]
    min_event = events[0]

    # Initialize counters
    mega = 0
    large = 0
    medium = 0
    small = 0
    early_events = 0
    late_events = 0
    alerts = []

    # Run the for loop on the 'events' list
    for e in events:
        p = e["participants"]
        t = e["time"]

        # Add participants to total
        total += p

        # Update max_event and min_event
        if p > max_event["participants"]:
            max_event = e
        if p < min_event["participants"]:
            min_event = e

        # Classify events
        if p >= 300:
            mega += 1
        elif p >= 150:
            large += 1
        elif p >= 75:
            medium += 1
        else:
            small += 1

        hour = int(t[:2])
        minute = int(t[3:])

        # Count early morning events
        if hour < 8:
            early_events += 1

        # Detect late events
        if hour > 10 or (hour == 10 and minute > 30):
            late_events += 1
            alerts.append("⚠️ " + e["location"] + ": Ceremony scheduled late")

        # Detect low engagement
        if p < 30:
            alerts.append("⚠️ " + e["location"] + ": Low engagement detected")

    # Calculate average participants
    average = total // n

    # Decide celebration status
    if total >= 1500:
        status = "National Pride Celebration"
    elif total >= 800:
        status = "Grand Celebration 🎉"
    else:
        status = "Local Celebration 😊"

    # Final Report
    print("\n 🎉 REPUBLIC DAY FLAG HOISTING ANALYTICS REPORT 🎉")

    print("\n📊 SUMMARY")
    print("➡️ Total Locations:", n)
    print("👥 Total Participants:", total)
    print("📈 Average Participants per Location:", average)

    print("\n----------------------------------------------------------------")

    print("\n🏆 HIGHEST PARTICIPATION")
    print("🥇", max_event["location"], "-", max_event["participants"], "participants")

    print("\n----------------------------------------------------------------")

    print("\n🔻 LOWEST PARTICIPATION")
    print("⚠️", min_event["location"], "-", min_event["participants"], "participants")

    print("\n----------------------------------------------------------------")

    print("\n📌 EVENT CLASSIFICATION")
    print("🌟 Mega Events  :", mega)
    print("🎈 Large Events :", large)
    print("🎯 Medium Events:", medium)
    print("🔹 Small Events :", small)

    print("\n----------------------------------------------------------------")

    print("\n⏰ TIME INSIGHTS")
    print("🌅 Early Morning Events:", early_events)
    print("🌙 Late Events:", late_events)

    print("\n----------------------------------------------------------------")

    print("\n🚨 ALERTS")
    if len(alerts) == 0:
        print("✅ No risks detected. All events are well planned.")
    else:
        for a in alerts:
            print(a)

    print("\n----------------------------------------------------------------")

    print("\n🏁 OVERALL CELEBRATION STATUS")
    print("🎊", status)

    print("\n----------------------------------------------------------------")

    print("\n💬 MESSAGE")
    print("✨ Unity, discipline, and participation make our nation strong.")
    print("🎉 Happy Republic Day! 🎉")
    print("🙏 JAI HIND 🙏")