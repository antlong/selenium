Improved Selenium 1 bindings.
====================================================
by Anthony Long.

Whats different?
================

Functionality:
--------------

::
	Ability to switch to any other active session.
	Ability to intelligently kill other sessions: Will not end current session if another ID is specified.
		New calls:
			get_current_session_id
			get_all_active_session_ids
			switch_to_session
			kill_session
		
	Create an 'on_error' method, that will be ran whenever you encounter a failure.
		New calls:
			selenium.on_error = your_func
	
	Add headers, and view your current headers.
		New calls:
			add_headers
			view_headers
	
	True implicit waits for all functions that take a locator.
		New calls:
			This is done automatically for you.
	
	Wait for things to happen with:
		wait_for_element
		wait_for_element_to_disappear
		wait_until
		wait_for_attribute
		wait_for_attribute_to_disappear