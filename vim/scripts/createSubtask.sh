#!/bin/bash

tee /tmp/jiraTemplate << END
fields:
  project:
    key: INTS
  summary: >- 
    CHANGE HERE
  priority:
    name: Medium
  components: # Values: Action Points, Business Testing, Technical Story, 
    - name: 
  description: |~
    
  assignee:
    name: 
  reporter:
    name: m9338
  issuetype:
    name: Sub-task
  parent:
    key: $1
END

jira subtask $1 -t /tmp/jiraTemplate  

