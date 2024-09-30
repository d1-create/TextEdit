package ui;

import java.awt.LayoutManager;

import javax.swing.BoxLayout;
import javax.swing.JFrame;

//main container containing all other components
public class maincontainer extends JFrame{
    @Override
    public void setLayout(LayoutManager manager) {
        super.setLayout(new BoxLayout(this, BoxLayout.X_AXIS));
    }
    
}
