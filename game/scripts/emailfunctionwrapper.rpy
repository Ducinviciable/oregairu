init:
    python:
        fourth_m = ""
        third_m = ""
        second_m = ""
        first_m = ""
        fourth_subject = ""
        third_subject = ""
        second_subject = ""
        first_subject = ""
        third_sender = ""
        second_sender = ""
        first_sender = ""
        #x y structure? .x .y

        base_height = 126 + 46

        chat_box_height = 297
        clearance = 25
        nm_bottom_loc = 1040 - chat_box_height - clearance
            #758. This is a constant.
        second_m_loc = 0
        third_m_loc = 0
        fourth_m_loc = 0
        new_message_height = 0

#All conversations are with hachiman as far as I know.
#call the function using the regular "say" identifiers. (ie, hachiman, yui, haruno, yumiko)
label mail_function(partner, sender, subjectline, message): #recall sender is required to put the text on left or right. Hachiman sent texts are on the left.

    #Queue up the locations of the old messages.
    python: #these are old message heights
        fourth_m_loc = third_m_loc - new_message_height
        third_m_loc = second_m_loc - new_message_height
        second_m_loc = nm_bottom_loc - new_message_height

    $new_message_height = base_height

    #Parse message to get the length of the message
    python:
        warpLen = len(textwrap.wrap(message, 28))
        for i in range(warpLen):
            new_message_height = new_message_height + 60

        if warpLen < 4:
            new_message_height = new_message_height + 20 * warpLen


    #The mail needs to placed such that when it moves up new_message_height
    #there is 25 units of clearance between the bottom and the chat box.
    #That means the mail is at chat_box height + clearance + length of message
        #the top of chat box is at: 1080 - 297 = 783
        #25 unit clearance => 758
        #the bottom of the message will be at 758
        #so top of message (anchor) will be at 758 - height of message
        #and since movement is length new_message_height
        #the locaton of all new messages is AT 758

    #queuing the messages
    python:
        fourth_m = third_m
        third_m = second_m
        second_m = first_m
        first_m = message

        fourth_subject = third_subject
        third_subject = second_subject
        second_subject = first_subject
        first_subject = subjectline

    #determining the display name
    #Convo's with yui
    if (partner == "yui"):
        if sender == "yui":
            $sender_name = "☆★Yui★☆"
        else:
            $sender_name = "Hikki♥"

    #Place cases for other text partners . I believe Miura and Haruno are possible conversation partners according to the script
    #see _mail.scx.txt

    elif (partner == "haruno"):
        if sender == "haruno":
            $sender_name = "Yukinoshita Haruno"
        else:
            $sender_name = "Hikigaya Hachiman"

    elif (partner == "yumiko"):
        if sender == "yumiko":
            $sender_name = "Yumiko☆"
        else:
            $sender_name = "Hikigaya Hachiman" #??? Hikio?

    elif (partner == "haruno"):
        if sender == "haruno":
            $sender_name = "Yukinoshita Haruno"
        else:
            $sender_name = "Hikigaya Hachiman"

    python:
        fourth_sender = third_sender
        third_sender = second_sender
        second_sender = first_sender
        first_sender = sender_name

    #☆★ゆい★☆：
    #雪ノ下陽乃
    #ｙｕmｉｋｏ☆
    #ヒッキー①
    #比企谷八幡

    #Take care of first and second messages. Probably need some sort of method to clear
    # the queue (have only seen Yukino Route which only has emails in one seen
    # but possibly other routes the variables will remain
    hide screen oldest_text
    hide screen older_text
    hide screen old_text
    hide screen new_text
    show screen new_text(first_sender, first_subject, first_m)
    #Check that the message is not empty
    if second_m:
        show screen old_text(second_sender, second_subject, second_m)
    if third_m:
        show screen older_text(third_sender, third_subject, third_m)
    if fourth_m:
        show screen oldest_text(fourth_sender, fourth_subject, fourth_m)
    return

label mail_hide:
    hide screen oldest_text
    hide screen older_text
    hide screen old_text
    hide screen new_text
    with dissolve
    return

label mail_clear:
    hide screen oldest_text
    hide screen older_text
    hide screen old_text
    hide screen new_text
    with dissolve
    python:
        fourth_m = ""
        third_m = ""
        second_m = ""
        first_m = ""
        fourth_subject = ""
        third_subject = ""
        second_subject = ""
        first_subject = ""
        fourth_sender = ""
        third_sender = ""
        second_sender = ""
        first_sender = ""
    return
