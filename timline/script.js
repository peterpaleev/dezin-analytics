// script.js

// Define the tasks (items)
var items = new vis.DataSet([
    // Phase 1: Quick Wins
    {id: 1, content: 'Improve Clarity and CTA Placement', start: '2023-10-09', end: '2023-10-10', group: 'Phase 1', className: 'high-priority'},
    {id: 2, content: 'Trust Badges and Certifications', start: '2023-10-11', end: '2023-10-12', group: 'Phase 1', className: 'high-priority'},
    {id: 3, content: 'Simplify Forms', start: '2023-10-13', end: '2023-10-17', group: 'Phase 1', className: 'high-priority'},
    {id: 4, content: 'Customer Testimonials and Case Studies', start: '2023-10-18', end: '2023-10-24', group: 'Phase 1', className: 'high-priority'},
    {id: 5, content: 'Social Proof through Clients', start: '2023-10-18', end: '2023-10-24', group: 'Phase 1', className: 'high-priority'},
  
    // Phase 2: Testing and Iteration
    {id: 6, content: 'Test Discount/Free Trial Offers', start: '2023-10-25', end: '2023-11-15', group: 'Phase 2', className: 'medium-priority'},
    {id: 7, content: 'Develop Industry-Specific Use Cases', start: '2023-10-25', end: '2023-11-15', group: 'Phase 2', className: 'medium-priority'},
    {id: 8, content: 'Test Different CTA Text', start: '2023-10-25', end: '2023-11-08', group: 'Phase 2', className: 'medium-priority'},
  
    // Phase 3: Strategic and Long-term Initiatives
    {id: 9, content: 'Video Production', start: '2023-11-16', end: '2024-01-31', group: 'Phase 3', className: 'medium-priority'},
    {id: 10, content: 'Interactive Product Calculator/Demo', start: '2023-11-16', end: '2024-02-15', group: 'Phase 3', className: 'medium-priority'},
    {id: 11, content: 'Form Progressive Disclosure', start: '2023-11-16', end: '2023-12-15', group: 'Phase 3', className: 'medium-priority'},
    {id: 12, content: 'Exit-Intent Popups', start: '2023-11-16', end: '2024-01-31', group: 'Phase 3', className: 'low-priority'},
  ]);
  
  // Define the phases (groups)
  var groups = new vis.DataSet([
    {id: 'Phase 1', content: 'Phase 1: Quick Wins'},
    {id: 'Phase 2', content: 'Phase 2: Testing and Iteration'},
    {id: 'Phase 3', content: 'Phase 3: Strategic Initiatives'},
  ]);

  // Get the timeline container
var container = document.getElementById('timeline');

// Set timeline options
var options = {
  stack: false,
  groupOrder: 'id',   // Order by group id
  editable: false,
  margin: {
    item: 20,
    axis: 40,
  },
  orientation: 'top',
};

// Create the timeline
var timeline = new vis.Timeline(container, items, groups, options);
