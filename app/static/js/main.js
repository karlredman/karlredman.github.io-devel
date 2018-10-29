/*
 *$(function() {
 *    alert( 'JavaScript Loaded!' );
 *});
 */


/*
 *if ($(window).width() < 960) {
 *    alert('Less than 960');
 *}
 *else {
 *    alert('More than 960');
 *}
 */

/* open all accordian items if large screen */
//if ($(window).width() > 600 ) {
if ($(window).width() > 960 ) {
    $("input[type='checkbox']").attr("checked", true);
}

/* open about page accordians (doesn't work on android phone) */
var pathname = window.location.pathname;
if( pathname.indexOf('about') >= 0){
    $("input[type='checkbox']").attr("checked", true);
    //alert(pathname);
}

/* WIP: want to open the contact_info accordian and send people there 
 * this might work: http://stackoverflow.com/questions/4482074/how-to-use-jquery-trigger-anchors-default-click-event
 * about location focus: http://stackoverflow.com/questions/6068266/jquery-how-to-trigger-anchor-links-click-event
 * */
$("#open_contact_info").click(function () {
    $("input:checkbox").prop('checked', true);
});
