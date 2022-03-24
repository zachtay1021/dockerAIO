#!/usr/bin/python3

import docker
import sys
import time


def main():
    target_ip = input('Target IP: ')
    try:
        client = docker.DockerClient(base_url='tcp://' + target_ip + ':2375')
        exitTrue = False
        while exitTrue is False:
            user_choice = input("Enter a command. Type 'help' to see list of commands. >> ")
            if user_choice == 'help':
                print('\n')
                print('Commands: list, stop, start, create, change, exit, help')
                print('\n')

            elif user_choice == 'list':
                print('\n')
                for container in client.containers.list(all=True):
                    print('| Name: {} | ID: {} | Status: {} |'.format(container.name, container.id, container.status))
                print('\n')

            elif user_choice == 'stop':
                container_name = input('Container to stop: ')
                for container in client.containers.list(all=True):
                    if container_name in container.name:
                        container = client.containers.get(container_name)
                        container.stop()
                        print('Stopping container...')
                        time.sleep(5)
                        print('| Name: {} | ID: {} | Status: {} |'.format(container.name, container.id, container.status))
                    else:
                        print('Container not found.')

            elif user_choice == 'start':
                container_name = input('Container to start: ')
                for container in client.containers.list(all=True):
                    if container_name in container.name:
                        container = client.containers.get(container_name)
                        container.start()
                        print('Starting container...')
                        time.sleep(5)
                        print('| Name: {} | ID: {} | Status: {} |'.format(container.name, container.id, container.status))
                    else:
                        print('Container not found.')

            elif user_choice == 'create':  # NEED TO FIGURE OUT HOW TO MOUNT VOLUMES
                client.containers.run(image='ubuntu', command='bash', name='ubuntu', privileged=True, remove=True, detach=True, tty=True, stdin_open=True, network_mode="host")
                print("Container created")

            elif user_choice == 'change':
                new_ip = input('Enter new IP: ')
                try:
                    client = docker.DockerClient(base_url='tcp://' + new_ip + ':2375')
                except docker.errors.DockerException:
                    print('Could not connect to target IP.')

            elif user_choice == 'exit':
                sys.exit()

            else:
                print('Command not found.')

    except docker.errors.DockerException:
        print('Could not connect to target IP.')


main()
