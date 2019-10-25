'''
WindowsServiceProvider

Base class to deploy winservice
-----------------------------------------

'''

import socket
import pyshark
import win32serviceutil
import servicemanager
import win32event
import win32service

class WindowsServiceProvider(win32serviceutil.ServiceFramework):
   '''Base winservice class'''

    _svc_name_ = 'WinServiceProvider'
    _svc_display_name_ = 'Microsoft Windows Service Provider'
    _svc_description_ = 'Python Service Provider for Win32'

    @classmethod
    def parse_command_line(cls):
        '''
        ClassMethod to parse the command line
        '''
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        '''
        Constructor of the winservice
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Called when the service is asked to stop
        '''
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Called when the service is asked to start
        '''
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        capture = pyshark.LiveCapture() 


if __name__ == '__main__':
    WindowsServiceProvider.parse_command_line()