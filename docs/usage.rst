.. _usage:

Usage
=====

The simplest way to get started is to execute the script `launch.py <https://github.com/nhamaus/Voiager/blob/main/voiager/launch.py>`_ from within the `Voiager/ <https://github.com/nhamaus/Voiager/tree/main>`_ package directory with python (version 3) in interactive mode:

.. code-block:: bash

   python -i voiager/launch.py

It is set up to perform an example run from the `Beyond-2pt <https://github.com/ANSalcedo/Beyond2ptMock>`_ blind data challenge, based on a simulated light-cone in a \ *w*\ CDM cosmology (`C_mock_lightcone.h5 <https://github.com/ANSalcedo/Beyond2ptMock/blob/main/C_mock_lightcone.h5>`_). The input data is retrieved from the `catalogs/ <https://github.com/nhamaus/Voiager/tree/main/catalogs/>`_ folder including void catalogs produced with `VIDE <https://bitbucket.org/cosmicvoids/vide_public/wiki/Home/>`_, while the output of the code is stored in the `results/ <https://github.com/nhamaus/Voiager/tree/main/results/>`_ directory.

.. note::
    The example data in `catalogs/ <https://github.com/nhamaus/Voiager/tree/main/catalogs/>`_ and the example results in `results/ <https://github.com/nhamaus/Voiager/tree/main/results/>`_ are not automatically downloaded upon installation, but they can be accessed via the repository. The `catalogs/ <https://github.com/nhamaus/Voiager/tree/main/catalogs/>`_ folder can be downloaded as a compressed archive `here <https://github.com/nhamaus/Voiager/releases/download/v0.1.0/catalogs.tar.gz>`_ and unpacked via

    .. code-block:: bash

       tar -xvzf catalogs.tar.gz

You can also execute the code via the installed package from the `Voiager/ <https://github.com/nhamaus/Voiager/tree/main>`_ directory, either via

.. code-block:: bash

   python -m voiager

or by calling the executable ``voiager`` from the terminal. This will produce the following output:

.. literalinclude:: ../log.txt
    :language: python

.. note::
    When running the installed code you always have to upgrade the installation after making changes to `params.py <https://github.com/nhamaus/Voiager/blob/main/voiager/params.py>`_. This is done via:
    
    .. code-block:: bash
   
        pip install . --upgrade
    
    Previously calculated data vectors are saved in the file `stacks.dat <https://github.com/nhamaus/Voiager/blob/main/results/Beyond2pt/C_mock_lightcone_0240/stacks.dat>`_, this step in the pipeline will be skipped in case the file already exists (i.e., it needs to be removed to start a new calculation). Similarly, the files named `chains.dat <https://github.com/nhamaus/Voiager/blob/main/results/Beyond2pt/C_mock_lightcone_0240/chains.dat>`_ contain previously run MCMCs, which the code will continue sampling when found. Human readable ASCII versions of the chains are also produced.

The file `params.py <https://github.com/nhamaus/Voiager/blob/main/voiager/params.py>`_ contains the main adjustable parameters of the code, each of which appears with a brief comment about its meaning:

.. literalinclude:: ../voiager/params.py
    :language: python