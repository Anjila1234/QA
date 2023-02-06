#Login page should be work properly
#Forgot password features should work properly
class login:
    url='https://opensource-demo.orangehrmlive.com/'
    username_boxid='txtUsername'
    password_boxid='txtPassword'
    login_clickbox='btnLogin'
    welcome_box='welcome'
    email_forget='//*[@id="forgotPasswordLink"]/a/font/font'
    orangehrm_usernameboxid='securityAuthentication_userName'
    reset_boxid='btnSearchValues'
    cancel_boxid='btnCancel'
#Fill the details to assigne the leave
class logout:
    forlogout='//*[@id="welcome'
    logoutposition='//*[@id="welcome-menu"]/ul/li[3]/a'
class dashbaord:
    assigneleave_box='//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[1]/div/a/img'
    employeename_boxid='assignleave_txtEmployee_empName'
    leavetype_box='//*[@id="assignleave_txtLeaveType"]/option[4]'
    leavebalance_box=''
    fromdate_box='assignleave_txtFromDate'
    todate_box='assignleave_txtToDate'
    comment_box='assignleave_txtComment'
    assignbutton_box='assignBtn'
#007-employee can check and add his own timesheet



