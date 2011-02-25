Improved Selenium 1 bindings.
====================================================
by Anthony Long.

Whats New?
================

Functionality:
--------------

::

	Switch to any other active session.
	Intelligently kill other sessions, will not end current session if another session ID is specified.
		New calls:
			get_current_session_id
			get_active_session_ids
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


What's coming up?
=================

1: Built in, intelligent support for javascript libraries such as Moo Tools, Prototype and more.
2: Better methods for validating attributes.