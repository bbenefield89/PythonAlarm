from utils.LinuxAlarm import LinuxAlarm


class PlatformAlarmFactory:
    @staticmethod
    def createNewPlatformAlarm(platform):
        platformAlarm = None

        if platform == 'Linux':
            platformAlarm = LinuxAlarm()

        elif platform == 'Darwin':
            platformAlarm = DarwinAlarm()

        elif platform == 'Windows':
            platformAlarm = WindowsAlarm()

        return platformAlarm
